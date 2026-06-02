#include "../include/JMOT.h"
int get_attitude(const std::string& key) {
    const auto it = ATTITUDE.find(key);
    if (it != ATTITUDE.end()) {
        return it->second;
    }
    throw std::invalid_argument("Invalided attitude input" + key);
}

int get_translation(const std::string& key) {
    const auto tran = TRANSLATE.find(key);
    if (tran != TRANSLATE.end()) {
        return tran->second;
    }
    throw std::invalid_argument("Invalided translation input"+key);
}

int get_headmode(const std::string &key) {
    const auto it = HEADMODE.find(key);
    if (it != HEADMODE.end()) {
        return it->second;
    }
    throw std::invalid_argument("Invalided head mode input"+key);
}

