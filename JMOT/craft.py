from JMOT import connect
from typing import Literal

def tuple2list(vec:tuple[float, float, float])->list[float, float, float]:
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return vec

class info:
    def get_name(socket)->str:
        rec = connect.send_message(f"true<<79", socket)
        return rec[0][0]
    def get_name_of_target(socket)->str:
        rec = connect.send_message(f"true<<81", socket)
        return rec[0][0]
    def name_of_craftID(craft_ID:int, socket)->str:
        rec = connect.send_message(f"true<<104<<{craft_ID}", socket)
        return rec[0][0]
    def part_count_of_craftID(craft_ID:int, socket)->int:
        rec = connect.send_message(f"true<<105<<{craft_ID}", socket)
        return rec[0][0]
    def craftID_of_craftname(craft_name:str, socket)->int:
        rec = connect.send_message(f"true<<105<<{craft_name}", socket)
        return rec[0][0]

class time:
    def time_since_launch(socket)->float:
        rec = connect.send_message(f"true<<75", socket)
        return rec[0][0]
    def total_time(socket)->float:
        rec = connect.send_message(f"true<<76", socket)
        return rec[0][0]

class performance:
    def get_battery(socket)->float:
        rec = connect.send_message(f"true<<8", socket)
        return rec[0][0]
    def get_stage_fuel(socket)->float:
        rec = connect.send_message(f"true<<9", socket)
        return rec[0][0]
    def get_mono_fuel(socket)->float:
        rec = connect.send_message(f"true<<10", socket)
        return rec[0][0]
    def get_engine_thrust(socket)->float:
        rec = connect.send_message(f"true<<19", socket)
        return rec[0][0]
    def get_mass(socket)->float:
        rec = connect.send_message(f"true<<20", socket)
        return rec[0][0]
    def get_max_engine_thrust(socket)->float:
        rec = connect.send_message(f"true<<23", socket)
        return rec[0][0]
    def get_TWR(socket)->float:
        rec = connect.send_message(f"true<<24", socket)
        return rec[0][0]
    def get_ISP(socket)->float:
        rec = connect.send_message(f"true<<25", socket)
        return rec[0][0]
    def get_stage_delta_v(socket)->float:
        rec = connect.send_message(f"true<<26", socket)
        return rec[0][0]
    def get_stage_burn_time(socket)->float:
        rec = connect.send_message(f"true<<27", socket)
        return rec[0][0]
    def get_craft_mass(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<103<<{craft_ID}", socket)
        return rec[0][0]

class position:
    def ECI_position(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<28", socket)
        vec = tuple2list(rec[0])
        return vec
    def target_ECI_position(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<29", socket)
        vec = tuple2list(rec[0])
        return vec
    def craft_ECI_position(craft_ID:int, socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<107<<{craft_ID}", socket)
        vec = tuple2list(rec[0])
        return vec

class attitude:
    def craft_heading(socket)->float:
        rec = connect.send_message(f"true<<30", socket)
        return rec[0]
    def craft_pitching(socket)->float:
        rec = connect.send_message(f"true<<31", socket)
        return rec[0]
    def craft_autopilot_heading(socket)->float:
        rec = connect.send_message(f"true<<32", socket)
        return rec[0]
    def craft_autopilot_pitching(socket)->float:
        rec = connect.send_message(f"true<<33", socket)
        return rec[0]
    def craft_bank_angle(socket)->float:
        rec = connect.send_message(f"true<<34", socket)
        return rec[0]
    def craft_AOA(socket)->float:
        rec = connect.send_message(f"true<<35", socket)
        return rec[0]
    def craft_side_slip(socket)->float:
        rec = connect.send_message(f"true<<36", socket)
        return rec[0]
    def craft_north_vector(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<37", socket)
        vec = tuple2list(rec[0])
        return vec
    def craft_east_vector(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<38", socket)
        vec = tuple2list(rec[0])
        return vec
    def craft_roll_axis(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<39", socket)
        vec = tuple2list(rec[0])
        return vec
    def craft_pitch_axis(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<40", socket)
        vec = tuple2list(rec[0])
        return vec
    def craft_yaw_axis(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<41", socket)
        vec = tuple2list(rec[0])
        return vec

class velocity:
    def surface_velocity(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<42", socket)
        vec = tuple2list(rec[0])
        return vec
    def orbit_velocity(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<43", socket)
        vec = tuple2list(rec[0])
        return vec
    def target_velocity(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<44", socket)
        vec = tuple2list(rec[0])
        return vec
    def gravity(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<45", socket)
        vec = tuple2list(rec[0])
        return vec
    def drag(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<46", socket)
        vec = tuple2list(rec[0])
        return vec
    def acceleration(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<47", socket)
        vec = tuple2list(rec[0])
        return vec
    def angular(socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<48", socket)
        vec = tuple2list(rec[0])
        return vec
    def lateral_speed(socket)->float:
        rec = connect.send_message(f"true<<49", socket)
        return rec[0]
    def vertical(socket)->float:
        rec = connect.send_message(f"true<<50", socket)
        return rec[0]
    def mach_number(socket)->float:
        rec = connect.send_message(f"true<<51", socket)
        return rec[0]
    def craft_velocity(craft_ID:int, socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<108", socket)
        vec = tuple2list(rec[0])
        return vec

class orbit:
    def AGL(socket)->float:
        rec = connect.send_message(f"true<<1", socket)
        return rec[0]
    def ASL(socket)->float:
        rec = connect.send_message(f"true<<2", socket)
        return rec[0]
    def ASF(socket)->float:
        rec = connect.send_message(f"true<<3", socket)
        return rec[0]
    def apoapsis(socket)->float:
        rec = connect.send_message(f"true<<12", socket)
        return rec[0]
    def periapsis(socket)->float:
        rec = connect.send_message(f"true<<13", socket)
        return rec[0]
    def time_to_apoapsis(socket)->float:
        rec = connect.send_message(f"true<<14", socket)
        return rec[0]
    def time_to_periapsis(socket)->float:
        rec = connect.send_message(f"true<<15", socket)
        return rec[0]
    def eccentricity(socket)->float:
        rec = connect.send_message(f"true<<16", socket)
        return rec[0]
    def inclination(socket)->float:
        rec = connect.send_message(f"true<<17", socket)
        return rec[0]
    def period(socket)->float:
        rec = connect.send_message(f"true<<18", socket)
        return rec[0]
    def craft_ASL(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<100<<{craft_ID}", socket)
        return rec[0]
    def craft_apoapsis_position(craft_ID:int, socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<110<<{craft_ID}", socket)
        vec = tuple2list(rec[0])
        return vec
    def craft_periapsis_position(craft_ID:int, socket)->list[float, float, float]:
        rec = connect.send_message(f"true<<111<<{craft_ID}", socket)
        vec = tuple2list(rec[0])
        return vec
    def craft_period(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<112<<{craft_ID}", socket)
        return rec[0]
    def craft_inclination(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<115<<{craft_ID}", socket)
        return rec[0]
    def craft_eccentricity(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<116<<{craft_ID}", socket)
        return rec[0]
    def craft_mean_anomaly(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<117<<{craft_ID}", socket)
        return rec[0]
    def craft_mean_motion(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<118<<{craft_ID}", socket)
        return rec[0]
    def craft_periapsis_argument(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<119<<{craft_ID}", socket)
        return rec[0]
    def craft_right_ascension(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<120<<{craft_ID}", socket)
        return rec[0]
    def craft_true_anomaly(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<121<<{craft_ID}", socket)
        return rec[0]
    def craft_SMA(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<122<<{craft_ID}", socket)
        return rec[0]
    
class input:
    def roll(socket)->float:
        rec = connect.send_message(f"true<<52", socket)
        return rec[0]
    def pitch(socket)->float:
        rec = connect.send_message(f"true<<53", socket)
        return rec[0]
    def yaw(socket)->float:
        rec = connect.send_message(f"true<<54", socket)
        return rec[0]
    def throttle(socket)->float:
        rec = connect.send_message(f"true<<55", socket)
        return rec[0]
    def brake(socket)->float:
        rec = connect.send_message(f"true<<56", socket)
        return rec[0]
    def slider1(socket)->float:
        rec = connect.send_message(f"true<<57", socket)
        return rec[0]
    def slider2(socket)->float:
        rec = connect.send_message(f"true<<58", socket)
        return rec[0]
    def slider3(socket)->float:
        rec = connect.send_message(f"true<<59", socket)
        return rec[0]
    def slider4(socket)->float:
        rec = connect.send_message(f"true<<60", socket)
        return rec[0]
    def translate_foraward(socket)->float:
        rec = connect.send_message(f"true<<61", socket)
        return rec[0]
    def translate_right(socket)->float:
        rec = connect.send_message(f"true<<62", socket)
        return rec[0]
    def translate_up(socket)->float:
        rec = connect.send_message(f"true<<63", socket)
        return rec[0]
    def translate_mode(socket)->float:
        rec = connect.send_message(f"true<<64", socket)
        return rec[0]
    
class misc:
    def active_stage(socket)->int:
        rec = connect.send_message(f"true<<65", socket)
        return rec[0]
    def num_of_stage(socket)->int:
        rec = connect.send_message(f"true<<66", socket)
        return rec[0]
    def is_ground(socket)->bool:
        rec = connect.send_message(f"true<<67", socket)
        return rec[0]
    def ag_status(ag:int, socket)->bool:
        rec = connect.send_message(f"true<<151", socket)
        return rec[0]
    class funk:
        def get_float(funkexpression:str, socket)->float:
            rec = connect.send_message(f"true<<157<<{funkexpression}", socket)
            return rec[0]
        def get_bool(funkexpression:str, socket)->bool:
            rec = connect.send_message(f"true<<157<<{funkexpression}", socket)
            return bool(rec[0])
        def get_string(funkexpression:str, socket)->str:
            rec = connect.send_message(f"true<<157<<{funkexpression}", socket)
            return rec[0]
        def get_int(funkexpression:str, socket)->int:
            rec = connect.send_message(f"true<<157<<{funkexpression}", socket)
            return rec[0]
        def get_vector(funkexpression:str, socket)->list[float, float, float]:
            rec = connect.send_message(f"true<<157<<{funkexpression}", socket)
            return tuple2list(rec[0])