from JMOT import connect
from typing import Literal

def tuple2list(vec:tuple[float, float, float])->list[float, float, float]:
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return vec

class info:
    def get_name()->str:
        rec = connect.send_message(f"true<<79")
        return rec[0]
    def get_name_of_target()->str:
        rec = connect.send_message(f"true<<81")
        return rec[0]
    def name_of_craftID(craft_ID:int)->str:
        rec = connect.send_message(f"true<<104<<{craft_ID}")
        return rec[0]
    def part_count_of_craftID(craft_ID:int)->int:
        rec = connect.send_message(f"true<<105<<{craft_ID}")
        return rec[0]
    def craftID_of_craftname(craft_name:str)->int:
        rec = connect.send_message(f"true<<105<<{craft_name}")
        return rec[0]

class time:
    def time_since_launch()->float:
        rec = connect.send_message(f"true<<75")
        return rec[0]
    def total_time()->float:
        rec = connect.send_message(f"true<<76")
        return rec[0]

class performance:
    def get_battery()->float:
        rec = connect.send_message(f"true<<8")
        return rec[0]
    def get_stage_fuel()->float:
        rec = connect.send_message(f"true<<9")
        return rec[0]
    def get_mono_fuel()->float:
        rec = connect.send_message(f"true<<10")
        return rec[0]
    def get_engine_thrust()->float:
        rec = connect.send_message(f"true<<19")
        return rec[0]
    def get_mass()->float:
        rec = connect.send_message(f"true<<20")
        return rec[0]
    def get_max_engine_thrust()->float:
        rec = connect.send_message(f"true<<23")
        return rec[0]
    def get_TWR()->float:
        rec = connect.send_message(f"true<<24")
        return rec[0]
    def get_ISP()->float:
        rec = connect.send_message(f"true<<25")
        return rec[0]
    def get_stage_delta_v()->float:
        rec = connect.send_message(f"true<<26")
        return rec[0]
    def get_stage_burn_time()->float:
        rec = connect.send_message(f"true<<27")
        return rec[0]
    def get_craft_mass(craft_ID:int)->float:
        rec = connect.send_message(f"true<<103<<{craft_ID}")
        return rec[0]

class position:
    def ECI_position()->list[float, float, float]:
        rec = connect.send_message(f"true<<28")
        vec = tuple2list(rec[0])
        return vec
    def target_ECI_position()->list[float, float, float]:
        rec = connect.send_message(f"true<<29")
        vec = tuple2list(rec[0])
        return vec
    def craft_ECI_position(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<107<<{craft_ID}")
        vec = tuple2list(rec[0])
        return vec

class attitude:
    def craft_heading()->float:
        rec = connect.send_message(f"true<<30")
        return rec[0]
    def craft_pitching()->float:
        rec = connect.send_message(f"true<<31")
        return rec[0]
    def craft_autopilot_heading()->float:
        rec = connect.send_message(f"true<<32")
        return rec[0]
    def craft_autopilot_pitching()->float:
        rec = connect.send_message(f"true<<33")
        return rec[0]
    def craft_bank_angle()->float:
        rec = connect.send_message(f"true<<34")
        return rec[0]
    def craft_AOA()->float:
        rec = connect.send_message(f"true<<35")
        return rec[0]
    def craft_side_slip()->float:
        rec = connect.send_message(f"true<<36")
        return rec[0]
    def craft_north_vector()->list[float, float, float]:
        rec = connect.send_message(f"true<<37")
        vec = tuple2list(rec[0])
        return vec
    def craft_east_vector()->list[float, float, float]:
        rec = connect.send_message(f"true<<38")
        vec = tuple2list(rec[0])
        return vec
    def craft_roll_axis()->list[float, float, float]:
        rec = connect.send_message(f"true<<39")
        vec = tuple2list(rec[0])
        return vec
    def craft_pitch_axis()->list[float, float, float]:
        rec = connect.send_message(f"true<<40")
        vec = tuple2list(rec[0])
        return vec
    def craft_yaw_axis()->list[float, float, float]:
        rec = connect.send_message(f"true<<41")
        vec = tuple2list(rec[0])
        return vec

class velocity:
    def surface_velocity()->list[float, float, float]:
        rec = connect.send_message(f"true<<42")
        vec = tuple2list(rec[0])
        return vec
    def orbit_velocity()->list[float, float, float]:
        rec = connect.send_message(f"true<<43")
        vec = tuple2list(rec[0])
        return vec
    def target_velocity()->list[float, float, float]:
        rec = connect.send_message(f"true<<44")
        vec = tuple2list(rec[0])
        return vec
    def gravity()->list[float, float, float]:
        rec = connect.send_message(f"true<<45")
        vec = tuple2list(rec[0])
        return vec
    def drag()->list[float, float, float]:
        rec = connect.send_message(f"true<<46")
        vec = tuple2list(rec[0])
        return vec
    def acceleration()->list[float, float, float]:
        rec = connect.send_message(f"true<<47")
        vec = tuple2list(rec[0])
        return vec
    def angular()->list[float, float, float]:
        rec = connect.send_message(f"true<<48")
        vec = tuple2list(rec[0])
        return vec
    def lateral()->float:
        rec = connect.send_message(f"true<<49")
        return rec[0]
    def vertical()->float:
        rec = connect.send_message(f"true<<50")
        return rec[0]
    def mach_number()->float:
        rec = connect.send_message(f"true<<51")
        return rec[0]
    def craft_velocity(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<108")
        vec = tuple2list(rec[0])
        return vec

class orbit:
    def AGL()->float:
        rec = connect.send_message(f"true<<1")
        return rec[0]
    def ASL()->float:
        rec = connect.send_message(f"true<<2")
        return rec[0]
    def ASF()->float:
        rec = connect.send_message(f"true<<3")
        return rec[0]
    def apoapsis()->float:
        rec = connect.send_message(f"true<<12")
        return rec[0]
    def periapsis()->float:
        rec = connect.send_message(f"true<<13")
        return rec[0]
    def time_to_apoapsis()->float:
        rec = connect.send_message(f"true<<14")
        return rec[0]
    def time_to_periapsis()->float:
        rec = connect.send_message(f"true<<15")
        return rec[0]
    def eccentricity()->float:
        rec = connect.send_message(f"true<<16")
        return rec[0]
    def inclination()->float:
        rec = connect.send_message(f"true<<17")
        return rec[0]
    def period()->float:
        rec = connect.send_message(f"true<<18")
        return rec[0]
    def craft_ASL(craft_ID:int)->float:
        rec = connect.send_message(f"true<<100<<{craft_ID}")
        return rec[0]
    def craft_apoapsis_position(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<110<<{craft_ID}")
        vec = tuple2list(rec[0])
        return vec
    def craft_periapsis_position(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<111<<{craft_ID}")
        vec = tuple2list(rec[0])
        return vec
    def craft_period(craft_ID:int)->float:
        rec = connect.send_message(f"true<<112<<{craft_ID}")
        return rec[0]
    def craft_inclination(craft_ID:int)->float:
        rec = connect.send_message(f"true<<115<<{craft_ID}")
        return rec[0]
    def craft_eccentricity(craft_ID:int)->float:
        rec = connect.send_message(f"true<<116<<{craft_ID}")
        return rec[0]
    def craft_mean_anomaly(craft_ID:int)->float:
        rec = connect.send_message(f"true<<117<<{craft_ID}")
        return rec[0]
    def craft_mean_motion(craft_ID:int)->float:
        rec = connect.send_message(f"true<<118<<{craft_ID}")
        return rec[0]
    def craft_periapsis_argument(craft_ID:int)->float:
        rec = connect.send_message(f"true<<119<<{craft_ID}")
        return rec[0]
    def craft_right_ascension(craft_ID:int)->float:
        rec = connect.send_message(f"true<<120<<{craft_ID}")
        return rec[0]
    def craft_true_anomaly(craft_ID:int)->float:
        rec = connect.send_message(f"true<<121<<{craft_ID}")
        return rec[0]
    def craft_SMA(craft_ID:int)->float:
        rec = connect.send_message(f"true<<122<<{craft_ID}")
        return rec[0]
    
class input:
    def roll()->float:
        rec = connect.send_message(f"true<<52")
        return rec[0]
    def pitch()->float:
        rec = connect.send_message(f"true<<53")
        return rec[0]
    def yaw()->float:
        rec = connect.send_message(f"true<<54")
        return rec[0]
    def throttle()->float:
        rec = connect.send_message(f"true<<55")
        return rec[0]
    def brake()->float:
        rec = connect.send_message(f"true<<56")
        return rec[0]
    def slider1()->float:
        rec = connect.send_message(f"true<<57")
        return rec[0]
    def slider2()->float:
        rec = connect.send_message(f"true<<58")
        return rec[0]
    def slider3()->float:
        rec = connect.send_message(f"true<<59")
        return rec[0]
    def slider4()->float:
        rec = connect.send_message(f"true<<60")
        return rec[0]
    def translate_foraward()->float:
        rec = connect.send_message(f"true<<61")
        return rec[0]
    def translate_right()->float:
        rec = connect.send_message(f"true<<62")
        return rec[0]
    def translate_up()->float:
        rec = connect.send_message(f"true<<63")
        return rec[0]
    def translate_mode()->float:
        rec = connect.send_message(f"true<<64")
        return rec[0]
    
class misc:
    def active_stage()->int:
        rec = connect.send_message(f"true<<65")
        return rec[0]
    def num_of_stage()->int:
        rec = connect.send_message(f"true<<66")
        return rec[0]
    def is_ground()->bool:
        rec = connect.send_message(f"true<<67")
        return rec[0]
    def ag_status(ag:int)->bool:
        print("start")
        rec = connect.send_message(f"true<<151<<{ag}")
        print(rec)
        return rec[0]
    class funk:
        def get_float(funkexpression:str)->float:
            rec = connect.send_message(f"true<<157<<{funkexpression}")
            return rec[0]
        def get_bool(funkexpression:str)->bool:
            rec = connect.send_message(f"true<<157<<{funkexpression}")
            return bool(rec[0])
        def get_string(funkexpression:str)->str:
            rec = connect.send_message(f"true<<157<<{funkexpression}")
            return rec[0]
        def get_int(funkexpression:str)->int:
            rec = connect.send_message(f"true<<157<<{funkexpression}")
            return rec[0]
        def get_vector(funkexpression:str)->list[float, float, float]:
            rec = connect.send_message(f"true<<157<<{funkexpression}")
            return tuple2list(rec[0])
        
class convert: 
    def position2LLA(position:list[float, float, float])->list[float, float, float]:
        tmp = position[1]
        position[1] = position[2]
        position[2] = tmp
        vec = tuple(position)

        rec = connect.send_message(f"true<<153<<{vec}")
        return list(rec[0])