#ifndef JMOT_UTILS_H
#define JMOT_UTILS_H

#include <string>
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <mutex>
#include <tuple>

// 版本号
#define JMOT_VERSION "0.3.a1"

using Vector3d = std::tuple<double, double, double>;
inline void show_vector(const Vector3d& vec) {
    std::cout << std::get<0>(vec) << ", "
    << std::get<1>(vec) << ", "
    << std::get<2>(vec)
    << std::endl;
}

class JMOT_Logger {
public:
    enum Direction { SEND, RECEIVE, INFO, ERROR };

    static void init(const std::string& log_file_path = "");
    static void log(Direction dir, const std::string& msg);

    static void send(const std::string& msg) { log(SEND, msg); }
    static void receive(const std::string& msg) { log(RECEIVE, msg); }
    static void info(const std::string& msg) { log(INFO, msg); }
    static void error(const std::string& msg) { log(ERROR, msg); }

private:
    static std::ofstream log_file;
    static std::mutex log_mutex;
};

class MessageBuilder {
public:
    template<typename T>
    MessageBuilder& operator<<(const T& val) {
        // 匹配 Python 的 << 分隔符
        ss << "<<" << val;
        return *this;
    }

    // 特化：处理 Vector3d (自动转为 (x, y, z) 字符串)
    MessageBuilder& operator<<(const Vector3d& vec) {
        ss << "<<(" << std::get<0>(vec) << ", "
                   << std::get<1>(vec) << ", "
                   << std::get<2>(vec) << ")";
        return *this;
    }

    MessageBuilder& operator<<(std::ostream& (*manip)(std::ostream&)) {
        manip(ss);
        return *this;
    }

    std::string str() const {
        return ss.str();
    }

    explicit operator std::string() const { return str(); }

private:
    std::stringstream ss;
};

class ResponseParser {
public:
    // 构造函数：按照 << 进行精确分割
    explicit ResponseParser(const std::string& response) {
        std::stringstream ss(response);
        std::string item;

        // 以 '<' 为分隔符进行切分，与 Python 的 split("<<") 逻辑对齐
        while (std::getline(ss, item, '<')) {
            // getline 遇到 < 会停止，如果连续两个 <，item 会是空串
            // Python 端使用 if item.strip(): 过滤了空白项，我们这里也做同样处理
            if (!item.empty()) {
                tokens.push_back(item);
            }
        }
    }

    // 获取第 index 个参数 (从 0 开始)
    std::string get(const int index) const {
        if (index >= 0 && static_cast<size_t>(index) < tokens.size()) {
            return tokens[index];
        }
        return "";
    }

    bool getBool(const int index) const {
        const std::string val = get(index);
        return (val == "true" || val == "1");
    }

    int getInt(const int index, const int defaultVal = 0) const {
        try {
            return std::stoi(get(index));
        } catch (...) {
            return defaultVal;
        }
    }

    double getDouble(const int index, const double defaultVal = 0.0) const {
        try {
            return std::stod(get(index));
        } catch (...) {
            return defaultVal;
        }
    }

    // 获取向量 (解析 "(x, y, z)" 格式)
    Vector3d getVector(const int index) const {
        std::string val = get(index);
        double x = 0, y = 0, z = 0;

        size_t start = val.find('(');
        size_t end = val.find(')');
        if (start != std::string::npos && end != std::string::npos && end > start) {
            std::string inner = val.substr(start + 1, end - start - 1);
            std::stringstream vss(inner);
            char comma;
            vss >> x >> comma >> y >> comma >> z;
        }
        return std::make_tuple(x, y, z);
    }

    size_t size() const { return tokens.size(); }

private:
    std::vector<std::string> tokens;
};

#endif //JMOT_UTILS_H