from JMOT import connect
from typing import Literal
import datetime, sys

def tuple2list(vec:tuple[float, float, float])->list[float, float, float]:
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return vec

<<<<<<< HEAD
def list2tuple(vec:list[float, float, float])->tuple[float, float, float]:
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    vec = tuple(vec)
    return vec


class info:
    def name()->str:
        rec = connect.send_message(f"true<<200")
        return rec[0]
    def name_of_target()->str:
        rec = connect.send_message(f"true<<201")
        return rec[0]
    def craftname_of_craftID(craft_ID:int)->str:
        rec = connect.send_message(f"true<<202<<{craft_ID}")
        return rec[0]
    def part_count_of_craftID(craft_ID:int)->int:
        rec = connect.send_message(f"true<<203<<{craft_ID}")
        return rec[0]
    def craftID_of_craftname(craft_name:str)->int:
        rec = connect.send_message(f"true<<204<<{craft_name}")
        return rec[0]
    def planet_of_craft(craft_ID:int)->str:
        rec = connect.send_message(f"true<<205<<{craft_ID}")
        return rec[0]
    def is_destroyed(craft_ID:int)->bool:
        rec = connect.send_message(f"true<<206<<{craft_ID}")
        return rec[0]
    def is_player(craft_ID:int)->bool:
        rec = connect.send_message(f"true<<207<<{craft_ID}")
        return rec[0]
    def is_ground()->bool:
        rec = connect.send_message(f"true<<208")
        return rec[0]
    def craft_is_ground(craft_id:int)->bool:
        rec = connect.send_message(f"true<<209<<{craft_id}")
=======
def write_to_file(message:str):
    with open(r"JMOT\tran.log", "a", encoding="utf-8") as f:
        f.writelines(message + '\n')

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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        return rec[0]

class time:
    def time_since_launch()->float:
<<<<<<< HEAD
        rec = connect.send_message(f"true<<220")
        return rec[0]
    def total_time()->float:
        rec = connect.send_message(f"true<<221")
        return rec[0]
    def frame_delta_time()->float:
        rec = connect.send_message(f"true<<222")
        return rec[0]
    def warp_amount()->float:
        rec = connect.send_message(f"true<<223")
        return rec[0]
    def real_time()->float:
        rec = connect.send_message(f"true<<224")
        return rec[0]

class performance:
    def battery()->float:
        rec = connect.send_message(f"true<<225")
        return rec[0]
    def stage_fuel()->float:
        rec = connect.send_message(f"true<<226")
        return rec[0]
    def mono_fuel()->float:
        rec = connect.send_message(f"true<<227")
        return rec[0]
    def all_stage_fuel()->float:
        rec = connect.send_message(f"true<<228")
        return rec[0]
    def current_engine_thrust()->float:
        rec = connect.send_message(f"true<<229")
        return rec[0]
    def mass()->float:
        rec = connect.send_message(f"true<<230")
        return rec[0]
    def dry_mass()->float:
        rec = connect.send_message(f"true<<231")
        return rec[0]
    def fuel_mass()->float:
        rec = connect.send_message(f"true<<232")
        return rec[0]
    def max_engine_thrust()->float:
        rec = connect.send_message(f"true<<233")
        return rec[0]
    def TWR()->float:
        rec = connect.send_message(f"true<<234")
        return rec[0]
    def ISP()->float:
        rec = connect.send_message(f"true<<235")
        return rec[0]
    def stage_delta_v()->float:
        rec = connect.send_message(f"true<<236")
        return rec[0]
    def stage_burn_time()->float:
        rec = connect.send_message(f"true<<237")
        return rec[0]
    def craft_mass(craft_ID:int)->float:
        rec = connect.send_message(f"true<<238<<{craft_ID}")
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        return rec[0]

class position:
    def ECI_position()->list[float, float, float]:
<<<<<<< HEAD
        rec = connect.send_message(f"true<<250")
        vec = tuple2list(rec[0])
        return vec
    def target_ECI_position()->list[float, float, float]:
        rec = connect.send_message(f"true<<251")
        vec = tuple2list(rec[0])
        return vec
    def craft_ECI_position(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<252<<{craft_ID}")
=======
        rec = connect.send_message(f"true<<28")
        vec = tuple2list(rec[0])
        return vec
    def target_ECI_position()->list[float, float, float]:
        rec = connect.send_message(f"true<<29")
        vec = tuple2list(rec[0])
        return vec
    def craft_ECI_position(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<107<<{craft_ID}")
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        vec = tuple2list(rec[0])
        return vec

class attitude:
    def craft_heading()->float:
<<<<<<< HEAD
        rec = connect.send_message(f"true<<255")
        return rec[0]
    def craft_pitching()->float:
        rec = connect.send_message(f"true<<256")
        return rec[0]
    def craft_autopilot_heading()->float:
        rec = connect.send_message(f"true<<257")
        return rec[0]
    def craft_autopilot_pitching()->float:
        rec = connect.send_message(f"true<<258")
        return rec[0]
    def craft_bank_angle()->float:
        rec = connect.send_message(f"true<<259")
        return rec[0]
    def craft_AOA()->float:
        rec = connect.send_message(f"true<<260")
        return rec[0]
    def craft_side_slip()->float:
        rec = connect.send_message(f"true<<261")
        return rec[0]
    def craft_north_vector()->list[float, float, float]:
        rec = connect.send_message(f"true<<262")
        vec = tuple2list(rec[0])
        return vec
    def craft_east_vector()->list[float, float, float]:
        rec = connect.send_message(f"true<<263")
        vec = tuple2list(rec[0])
        return vec
    def craft_roll_axis()->list[float, float, float]:
        rec = connect.send_message(f"true<<264")
        vec = tuple2list(rec[0])
        return vec
    def craft_pitch_axis()->list[float, float, float]:
        rec = connect.send_message(f"true<<265")
        vec = tuple2list(rec[0])
        return vec
    def craft_yaw_axis()->list[float, float, float]:
        rec = connect.send_message(f"true<<266")
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        vec = tuple2list(rec[0])
        return vec

class velocity:
    def surface_velocity()->list[float, float, float]:
<<<<<<< HEAD
        rec = connect.send_message(f"true<<270")
        vec = tuple2list(rec[0])
        return vec
    def orbit_velocity()->list[float, float, float]:
        rec = connect.send_message(f"true<<271")
        vec = tuple2list(rec[0])
        return vec
    def target_velocity()->list[float, float, float]:
        rec = connect.send_message(f"true<<272")
        vec = tuple2list(rec[0])
        return vec
    def gravity()->list[float, float, float]:
        rec = connect.send_message(f"true<<273")
        vec = tuple2list(rec[0])
        return vec
    def drag()->list[float, float, float]:
        rec = connect.send_message(f"true<<274")
        vec = tuple2list(rec[0])
        return vec
    def acceleration()->list[float, float, float]:
        rec = connect.send_message(f"true<<275")
        vec = tuple2list(rec[0])
        return vec
    def angular()->list[float, float, float]:
        rec = connect.send_message(f"true<<276")
        vec = tuple2list(rec[0])
        return vec
    def lateral()->float:
        rec = connect.send_message(f"true<<277")
        return rec[0]
    def vertical()->float:
        rec = connect.send_message(f"true<<278")
        return rec[0]
    def mach_number()->float:
        rec = connect.send_message(f"true<<278")
        return rec[0]
    def craft_velocity(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<280")
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        vec = tuple2list(rec[0])
        return vec

class orbit:
    def AGL()->float:
<<<<<<< HEAD
        rec = connect.send_message(f"true<<290")
        return rec[0]
    def ASL()->float:
        rec = connect.send_message(f"true<<291")
        return rec[0]
    def ASF()->float:
        rec = connect.send_message(f"true<<292")
        return rec[0]
    def apoapsis()->float:
        rec = connect.send_message(f"true<<293")
        return rec[0]
    def periapsis()->float:
        rec = connect.send_message(f"true<<294")
        return rec[0]
    def apoapsis_time()->float:
        rec = connect.send_message(f"true<<295")
        return rec[0]
    def periapsis_time()->float:
        rec = connect.send_message(f"true<<296")
        return rec[0]
    def eccentricity()->float:
        rec = connect.send_message(f"true<<297")
        return rec[0]
    def inclination()->float:
        rec = connect.send_message(f"true<<298")
        return rec[0]
    def period()->float:
        rec = connect.send_message(f"true<<299")
        return rec[0]
    def craft_ASL(craft_ID:int)->float:
        rec = connect.send_message(f"true<<300<<{craft_ID}")
        return rec[0]
    def craft_apoapsis_position(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<301<<{craft_ID}")
        vec = tuple2list(rec[0])
        return vec
    def craft_periapsis_position(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<302<<{craft_ID}")
        vec = tuple2list(rec[0])
        return vec
    def craft_period(craft_ID:int)->float:
        rec = connect.send_message(f"true<<303<<{craft_ID}")
        return rec[0]
    def craft_apoapsis_time(craft_ID:int)->float:
        rec = connect.send_message(f"true<<304<<{craft_ID}")
        return rec[0]
    def craft_periapsis_time(craft_ID:int)->float:
        rec = connect.send_message(f"true<<305<<{craft_ID}")
        return rec[0]
    def craft_inclination(craft_ID:int)->float:
        rec = connect.send_message(f"true<<306<<{craft_ID}")
        return rec[0]
    def craft_eccentricity(craft_ID:int)->float:
        rec = connect.send_message(f"true<<307<<{craft_ID}")
        return rec[0]
    def craft_mean_anomaly(craft_ID:int)->float:
        rec = connect.send_message(f"true<<308<<{craft_ID}")
        return rec[0]
    def craft_mean_motion(craft_ID:int)->float:
        rec = connect.send_message(f"true<<309<<{craft_ID}")
        return rec[0]
    def craft_periapsis_argument(craft_ID:int)->float:
        rec = connect.send_message(f"true<<310<<{craft_ID}")
        return rec[0]
    def craft_right_ascension(craft_ID:int)->float:
        rec = connect.send_message(f"true<<311<<{craft_ID}")
        return rec[0]
    def craft_true_anomaly(craft_ID:int)->float:
        rec = connect.send_message(f"true<<312<<{craft_ID}")
        return rec[0]
    def craft_SMA(craft_ID:int)->float:
        rec = connect.send_message(f"true<<313<<{craft_ID}")
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        return rec[0]
    
class input:
    def roll()->float:
<<<<<<< HEAD
        rec = connect.send_message(f"true<<320")
        return rec[0]
    def pitch()->float:
        rec = connect.send_message(f"true<<321")
        return rec[0]
    def yaw()->float:
        rec = connect.send_message(f"true<<322")
        return rec[0]
    def throttle()->float:
        rec = connect.send_message(f"true<<323")
        return rec[0]
    def brake()->float:
        rec = connect.send_message(f"true<<324")
        return rec[0]
    def slider1()->float:
        rec = connect.send_message(f"true<<325")
        return rec[0]
    def slider2()->float:
        rec = connect.send_message(f"true<<326")
        return rec[0]
    def slider3()->float:
        rec = connect.send_message(f"true<<327")
        return rec[0]
    def slider4()->float:
        rec = connect.send_message(f"true<<328")
        return rec[0]
    def translate_foraward()->float:
        rec = connect.send_message(f"true<<329")
        return rec[0]
    def translate_right()->float:
        rec = connect.send_message(f"true<<330")
        return rec[0]
    def translate_up()->float:
        rec = connect.send_message(f"true<<331")
        return rec[0]
    def translate_mode()->float:
        rec = connect.send_message(f"true<<332")
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        return rec[0]
    def pitch_pids()->list[float, float, float]:
        rec = connect.send_message(f"true<<333")
        vec = tuple2list(rec[0])
        return vec
    def roll_pids()->list[float, float, float]:
        rec = connect.send_message(f"true<<334")
        vec = tuple2list(rec[0])
        return vec
    
class misc:
<<<<<<< HEAD
    def activing_stage()->int:
        rec = connect.send_message(f"true<<340")
        return rec[0]
    def num_of_stage()->int:
        rec = connect.send_message(f"true<<341")
        return rec[0]
    def ag_status(ag:int)->bool:
        print("start")
        rec = connect.send_message(f"true<<342<<{ag}")
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        return rec[0]
    def cast_ray(vec1:list[float, float, float], vec2:list[float, float, float])->list[float, float, float]:
        vec1 = list2tuple(vec1)
        vec2 = list2tuple(vec2)
        rec = connect.send_message(f"true<<343<<{vec1}<<{vec2}")
        vec = tuple2list(rec)
        return vec
    
    class funk:
        def get_float(funkexpression:str)->float:
<<<<<<< HEAD
            rec = connect.send_message(f"true<<344<<{funkexpression}")
            return rec[0]
        def get_bool(funkexpression:str)->bool:
            rec = connect.send_message(f"true<<344<<{funkexpression}")
            return bool(rec[0])
        def get_string(funkexpression:str)->str:
            rec = connect.send_message(f"true<<344<<{funkexpression}")
            return rec[0]
        def get_int(funkexpression:str)->int:
            rec = connect.send_message(f"true<<344<<{funkexpression}")
            return rec[0]
        def get_vector(funkexpression:str)->list[float, float, float]:
            rec = connect.send_message(f"true<<344<<{funkexpression}")
            return tuple2list(rec[0])

    class convert:
        def position2LL_AGL(position:list[float, float, float])->list[float, float, float]:
            vec = list2tuple(position)
            rec = connect.send_message(f"true<<345<<{vec}")
            return list(rec[0])
        def position2LL_ASL(position:list[float, float, float])->list[float, float, float]:
            vec = list2tuple(position)
            rec = connect.send_message(f"true<<346<<{vec}")
            return list(rec[0])
        def LL_AGL2position(position:list[float, float, float])->list[float, float, float]:
            rec = connect.send_message(f"true<<347<<{tuple(position)}")
            vec = tuple2list(rec[0])
            return vec
        def LL_ASL2position(position:list[float, float, float])->list[float, float, float]:
            rec = connect.send_message(f"true<<348<<{tuple(position)}")
            vec = tuple2list(rec[0])
            return vec
        
    
    def get_terrain_color(position:list[float, float, float])->list[float, float, float]:
        position = tuple(position)
        rec = connect.send_message(f"true<<349<<{position}")
        return list(rec[0])
    def get_terrain_height(position:list[float, float, float])->float:
        position = tuple(position)
        rec = connect.send_message(f"true<<350<<{position}")
        return rec[0]
    
    def solar_radition()->float:
        rec = connect.send_message(f"true<<351")
        return rec[0]
    
    def camera_position()->list[float, float, float]:
        rec = connect.send_message(f"true<<352")
        vec = tuple2list(rec)
        return vec
    def camera_pointing()->list[float, float, float]:
        rec = connect.send_message(f"true<<353")
        vec = tuple2list(rec)
        return vec
    def camera_direction()->list[float, float, float]:
        rec = connect.send_message(f"true<<354")
        vec = tuple2list(rec)
        return vec
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
