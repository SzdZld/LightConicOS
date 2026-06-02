#include "JMOT.h"

#define NAME "200"
#define TARGET_CRAFTNAME "201"
#define CRAFTNAME_OF_CRAFTID "202"
#define PART_COUNT_OF_CRAFTID "203"
#define CRAFTID_OF_CRAFTNAME "204"
#define PLANET_OF_CRAFT "205"

std::string JMOT::craft::info::name(const JMOT_Socket* sock) {
    std::string cmd = "true<<";
    cmd.append(NAME);
    const auto response = sock->sendCommand(cmd);
    return response.get(0);
}
std::string JMOT::craft::info::target_craftName(const JMOT_Socket* sock) {
    std::string cmd = "true<<";
    cmd.append(TARGET_CRAFTNAME);
    const auto response = sock->sendCommand(cmd);
    return response.get(0);
}
std::string JMOT::craft::info::craftName_of_craftID(int craft_id, const JMOT_Socket* sock) {
    std::string cmd = "true<<";
    cmd.append(CRAFTNAME_OF_CRAFTID);
    const auto response = sock->sendCommand(cmd);
    return response.get(0);
}
int JMOT::craft::info::part_count_of_craftID(int craft_id, const JMOT_Socket* sock) {
    std::string cmd = "true<<";
    cmd.append(PART_COUNT_OF_CRAFTID);
    const auto response = sock->sendCommand(cmd);
    return response.getInt(0);
}
int JMOT::craft::info::craftID_of_craftName(const std::string& craft_name, const JMOT_Socket* sock) {
    std::string cmd = "true<<";
    cmd.append(CRAFTID_OF_CRAFTNAME).append("<<").append(craft_name);
    const auto response = sock->sendCommand(cmd);
    return response.getInt(0);
}
std::string JMOT::craft::info::planet_of_craft(const int craft_id, const JMOT_Socket* sock) {
    std::string cmd = "true<<";
    cmd.append(PLANET_OF_CRAFT).append("<<").append(std::to_string(craft_id));
    const auto response = sock->sendCommand(cmd);
    return response.get(0);
}