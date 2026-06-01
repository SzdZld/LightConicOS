#include "../include/JMOT_utils.h"
#include <iostream>

std::ofstream JMOT_Logger::log_file;
std::mutex JMOT_Logger::log_mutex;

void JMOT_Logger::init(const std::string& log_file_path) {
    if (!log_file_path.empty()) {
        // ios::app 表示追加写入
        log_file.open(log_file_path, std::ios::app);
        if (log_file.is_open()) {
            std::cout << "logger debug on " << log_file_path << std::endl;
        } else {
            std::cerr << "WARNING: Failed to start or create log file: " << log_file_path << std::endl;
        }
    }
}

void JMOT_Logger::log(Direction dir, const std::string& msg) {
    std::lock_guard<std::mutex> lock(log_mutex);

    const auto now = std::chrono::system_clock::now();
    const auto time_t = std::chrono::system_clock::to_time_t(now);
    const auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()) % 1000;

    std::stringstream ss;
    ss << std::put_time(std::localtime(&time_t), "%Y-%m-%d %H:%M:%S")
       << "," << std::setfill('0') << std::setw(3) << ms.count();

    switch (dir) {
        case SEND:    ss << "-> "; break;
        case RECEIVE: ss << "<- "; break;
        case INFO:    ss << "[INFO]  "; std::cout << msg << std::endl; break;
        case ERROR:   ss << "[ERROR] "; std::cerr << msg << std::endl;break;
    }
    ss << msg;

    const std::string log_line = ss.str();

    if (log_file.is_open()) {
        log_file << log_line << std::endl;
        log_file.flush();
    }
}
