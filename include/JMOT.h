#ifndef JMOT_H
#define JMOT_H

#include "JMOT_utils.h"
#include "JMOT_client.h"

#include <string>
#include <map>
#include <stdexcept>

const std::map<std::string, int> ATTITUDE = {
    {"pitch", 1},
    {"yaw", 2},
    {"roll", 3}
};
int get_attitude(const std::string& key);

const std::map<std::string, int> TRANSLATE = {
    {"forward", 1},
    {"right", 2},
    {"up", 3},
    {"mode", 4}
};
int get_translation(const std::string& key);

const std::map<std::string, int> HEADMODE = {
    {"none",1},
    {"prograde",2},
    {"retrograde",3},
    {"target",4},
    {"burnmode",5},
    {"current",6},
};
int get_headmode(const std::string& key);

class JMOT {
public:
    class control {
        public:
            bool display(std::string msg);
            bool local_log(std::string msg);
            bool flight_log(std::string msg, bool override);
            bool active_stage();
            bool switch_craft(int craft_id);
            bool set_target(std::string target_name);
            bool set_ag(int active_group, bool status);
            bool set_attitude(std::string attitude, double value);
            bool set_throttle(double throttle);
            bool set_brake(double brake);
            bool set_pitching(double pitching);
            bool set_heading(double heading);
            bool set_slider(int slider, double value);
            bool set_heading_vector(Vector3d vector);
            bool set_translate(std::string translate, double value);
            bool lock_head_mode(std::string key);
            // bool set_variable(int part_id, std::string variable_name);
            // bool set_variable_list(std::string variable_name, double value);
            bool set_part_active(int part_id, bool part_status);
            bool set_part_focused(int part_id, bool part_focused);
            bool set_part_name(int part_id, const std::string& name);
            bool set_part_explode(int part_id, double explode_power);
            bool set_part_transfer(int part_id, double part_trans);
    };
    class craft {
        public:
        class info {
        public:
            static std::string name(const JMOT_Socket* sock);
            static std::string target_craftName(const JMOT_Socket* sock);
            static std::string craftName_of_craftID(int craft_id, const JMOT_Socket* sock);
            static int part_count_of_craftID(int craft_id, const JMOT_Socket* sock);
            static int craftID_of_craftName(const std::string& craft_name, const JMOT_Socket* sock);
            static std::string planet_of_craft(int craft_id, const JMOT_Socket* sock);
        };
        class fuel {
        public:
            double battery();
            double stage_fuel();
            double mono_fuel();
            double all_stage_fuel();
        };
        class performance {
        public:
            double current_engine_thrust();
            double mass();
            double dry_mass();
            double fuel_mass();
            double max_engine_thrust();
            double TWR();
            double ISP();
            double stage_delta_v();
            double stage_burn_time();
            double solar_radition();
            double craft_mass(int craft_id);
        };
        class attitude {
            public:
            double craft_heading();
            double craft_pitching();
            double craft_autopilot_heading();
            double craft_autopilot_pitching();
            double craft_bank_angle();
            double craft_AOA();
            double craft_side_slip();
            Vector3d craft_north_vector();
            Vector3d craft_east_vector();
            Vector3d craft_roll_axis();
            Vector3d craft_pitch_axis();
            Vector3d craft_yaw_axis();
        };
        class velocity {
            public:
            Vector3d surface_velocity();
            Vector3d orbit_velocity();
            Vector3d target_velocity();
            Vector3d gravity();
            Vector3d drag();
            Vector3d acceleration();
            Vector3d angular();
            double lateral();
            double vertical();
            double mach_number();
            Vector3d craft_velocity(int craft_id);
        };
        class position {
            public:
            double AGL();
            double ASL();
            double ASF();
            double craft_ASL();
            bool is_ground();
            bool craft_is_ground();
            Vector3d ECI_position();
            Vector3d target_position();
            Vector3d craft_ECI_position(int craft_id);

        };
        class orbit {
            public:
            double apoapsis();
            double periapsis();
            double time_to_apoapsis();
            double time_to_periapsis();
            double eccentricity();
            double inclination();
            double period();
            Vector3d craft_apoapsis_position(int craft_id);
            Vector3d craft_periapsis_position(int craft_id);
            double craft_period(int craft_id);
            double craft_time_to_apoapsis(int craft_id);
            double craft_time_to_periapsis(int craft_id);
            double craft_inclination(int craft_id);
            double craft_eccentricity(int craft_id);
            double craft_mean_anomaly(int craft_id);
            double craft_mean_motion(int craft_id);
            double craft_periapsis_argument(int craft_id);
            double craft_right_ascension(int craft_id);
            double craft_true_anomaly(int craft_id);
            double craft_SMA(int craft_id);
        };
        class input {
            public:
            double roll();
            double pitch();
            double yaw();
            double throttle();
            double brake();
            double slider1();
            double slider2();
            double slider3();
            double slider4();
            double translate_forward();
            double translate_right();
            double translate_up();
            double translate_mode();
            Vector3d pitch_pids();
            Vector3d roll_pids();
        };
        class status {
            public:
            int activing_stage();
            int num_of_stage();
            bool ag_status(int ag);
            bool craft_is_destroyed(int craft_id);
            bool craft_is_player(int craft_id);
        };
    };
    class part {
        public:
        class info {
            public:
            std::string partName_of_partID(int partID);
            int partID_of_partName(std::string partname);
            int this_partID(int partID);
            int min_partID(int partID);
            int max_partID(int partID);
            std::string part_type(int partID);
            bool is_part_active(int partID);
            double is_part_under_water(int partID);
        };
        class performance {
            public:
            double part_mass(int partID);
            double part_dry_mass(int partID);
            double part_fuel_mass(int partID);
            double part_temperature(int partID);
            double part_drag(int partID);
        };
        Vector3d part_position(int partID);
        Vector3d part_local_to_eci(int partID, Vector3d vector);
        Vector3d part_eci_to_local(int partID, Vector3d vector);
        // std::string get_variable(int partID, std::string variable_name);
        // std::string* part_name(int partID, std::string variable_name);
    };
    class planet {
        public:
        class info {
            public:
            double planet_mass(std::string planet_name);
            double planet_radius(std::string planet_name);
            bool is_solid_ground(std::string planet_name);
            double planet_SOI_radius(std::string planet_name);
            double planet_len_of_day(std::string planet_name);
            double planet_len_of_year(std::string planet_name);
            std::string planet_local_name();
            std::string target_planet(std::string planet_name);
            std::string planet_parent(std::string planet_name);
            std::string* planet_child_list(std::string planet_name);
            std::string* planet_craft_list(std::string planet_name);
            int* planet_craftID_list(std::string planet_name);
            std::string* planet_structure_list(std::string planet_name);
            Vector3d get_terrain_color(Vector3d planet_position);
        };
        class atmosphere {
            public:
            double air_density();
            double air_pressure();
            double speed_of_sound();
            double temperature();
            double atmosphere_air_density(std::string atmosphere_name);
            double atmosphere_height(std::string atmosphere_name);
            double atmosphere_fade_out(std::string atmosphere_name);
        };
        class orbit {
            public:
            Vector3d planet_solar_position(std::string planet_name);
            Vector3d planet_velocity(std::string planet_name);
            Vector3d planet_apoapsis_position(std::string planet_name);
            Vector3d planet_periapsis_position(std::string planet_name);
            double planet_period(std::string planet_name);
            double planet_time_to_apoapsis(std::string planet_name);
            double planet_time_to_periapsis(std::string planet_name);
            double planet_inclination(std::string planet_name);
            double planet_eccentricity(std::string planet_name);
            double planet_mean_anomaly(std::string planet_name);
            double planet_mean_motion(std::string planet_name);
            double planet_periapsis_argument(std::string planet_name);
            double planet_right_ascension(std::string planet_name);
            double planet_true_anomaly(std::string planet_name);
            double planet_SMA(std::string planet_name);
            double get_terrain_height(Vector3d position);
        };
    };
    class time {
        public:
        double time_since_launch();
        double total_time();
        double frame_delta_time();
        double warp_amount();
        double real_time();
        bool set_time_mode(int time_mode);
    };
    class misc {
        class convert {
            public:
            Vector3d position2LL_AGL(Vector3d position);
            Vector3d position2LL_ASL(Vector3d position);
            Vector3d LL_AGL2position(Vector3d position);
            Vector3d LL_ASL2position(Vector3d position);
            Vector3d cast_ray(Vector3d vector1, Vector3d vector2);
        };
        class camera {
            public:
            Vector3d camera_position();
            Vector3d camera_pointing();
            Vector3d camera_direction();
        };
        class funk {
            public:
            double get_float(std::string funk_expression);
            bool get_bool(std::string funk_expression);
            std::string get_string(std::string funk_expression);
            int get_int(std::string funk_expression);
            Vector3d get_vector(std::string funk_expression);
        };
    };
    class extra {
    };
};

#endif //JMOT_H
