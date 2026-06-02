#ifndef JMOT_CLIENT_H
#define JMOT_CLIENT_H

#include "JMOT_utils.h"

#ifdef _WIN32
    #include <winsock2.h>
    #include <ws2tcpip.h>
#else
    // 如果是 Linux/GCC 环境，包含 POSIX socket 头文件
    #include <sys/socket.h>
    #include <netinet/in.h>
    #include <arpa/inet.h>
    #include <unistd.h>
    #define INVALID_SOCKET (-1)
    #define SOCKET_ERROR (-1)
    #define closesocket(s) close(s)
    typedef int SOCKET;
#endif

#include <iostream>
#include <string>

class JMOT_Socket {
private:
    SOCKET sock;
    bool connected;
    int buffer_size;

public:
    JMOT_Socket() : sock(INVALID_SOCKET), connected(false), buffer_size(4096) {}

    ~JMOT_Socket() {
        if (connected && sock != INVALID_SOCKET) {
            closesocket(sock);
        }
#ifdef _WIN32
        WSACleanup();
#endif
    }

    /**
     * @brief 连接到服务器并初始化日志和版本校验
     */
    bool connect(const std::string& ip = "127.0.0.1",
                 int port = 10809,
                 int buf_size = 2048,
                 const std::string& log_file = "jmot_client.log"
                 )
    {
        this->buffer_size = buf_size;

#ifdef _WIN32
        // 仅在 Windows 下初始化 Winsock
        WSADATA wsaData;
        if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
            JMOT_Logger::error("Winsock initialize failure");
            return false;
        }
#endif
        // 1. 初始化日志记录功能
        JMOT_Logger::init(log_file);

        // 2. 创建 Socket
        sock = socket(AF_INET, SOCK_STREAM, 0);
        if (sock == INVALID_SOCKET) {
            JMOT_Logger::error("Create Socket Failed");
            return false;
        }

        // 3. 配置地址并发起连接
        sockaddr_in addr{};
        addr.sin_family = AF_INET;
        addr.sin_port = htons(port);
        addr.sin_addr.s_addr = inet_addr(ip.c_str());

        if (::connect(sock, reinterpret_cast<sockaddr *>(&addr), sizeof(addr)) == SOCKET_ERROR) {
            JMOT_Logger::error("connect to server [" + ip + ":" + std::to_string(port) + "] failed");
            return false;
        }
        connected = true;

        // 4. 发送 "version" 指令并检查回参
        const ResponseParser ver_res = sendCommand("version");
        const std::string server_version = ver_res.get(0); // 获取列表中的第一个元素

        if (server_version != JMOT_VERSION) {
            JMOT_Logger::error("version error, server version: " + server_version + ", client version: " + JMOT_VERSION);
            connected = false; // 版本不符，断开连接状态
            return false;
        }

        JMOT_Logger::info("JMOT v" + server_version + " connect successful");
        return true;
    }

    /**
     * @brief 发送指令并接收回复
     */
    ResponseParser sendCommand(const std::string& cmd) const {
        if (!connected || sock == INVALID_SOCKET) {
            JMOT_Logger::error("Send Failed");

            return ResponseParser("");
        }

        JMOT_Logger::send(cmd);
        if (send(sock, cmd.c_str(), static_cast<int>(cmd.length()), 0) == SOCKET_ERROR) {
            JMOT_Logger::error("Socket 发送数据异常");
            return ResponseParser("");
        }

        // 使用自定义的 buffer_size 接收回复
        std::string buffer(buffer_size, '\0');
        const int len = recv(sock, &buffer[0], buffer_size, 0);

        if (len <= 0) {
            JMOT_Logger::error("接收数据失败或连接已断开");
            return ResponseParser("");
        }

        // 截取实际接收到的长度，避免尾部乱码
        const std::string response = buffer.substr(0, len);
        JMOT_Logger::receive(response);

        return ResponseParser(response);
    }
};

#endif // JMOT_CLIENT_H