from JMOT import connect
from typing import Literal

def tuple2list(vec:tuple[float, float, float])->list[float, float, float]:
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return vec

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
        return rec[0]

class time:
    def time_since_launch()->float:
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
        return rec[0]

class position:
    def ECI_position()->list[float, float, float]:
        rec = connect.send_message(f"true<<250")
        vec = tuple2list(rec[0])
        return vec
    def target_ECI_position()->list[float, float, float]:
        rec = connect.send_message(f"true<<251")
        vec = tuple2list(rec[0])
        return vec
    def craft_ECI_position(craft_ID:int)->list[float, float, float]:
        rec = connect.send_message(f"true<<252<<{craft_ID}")
        vec = tuple2list(rec[0])
        return vec

class attitude:
    def craft_heading()->float:
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
        vec = tuple2list(rec[0])
        return vec

class velocity:
    def surface_velocity()->list[float, float, float]:
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
        vec = tuple2list(rec[0])
        return vec

class orbit:
    def AGL()->float:
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
        return rec[0]
    
class input:
    def roll()->float:
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
    def activing_stage()->int:
        rec = connect.send_message(f"true<<340")
        return rec[0]
    def num_of_stage()->int:
        rec = connect.send_message(f"true<<341")
        return rec[0]
    def ag_status(ag:int)->bool:
        print("start")
        rec = connect.send_message(f"true<<342<<{ag}")
        return rec[0]
    def cast_ray(vec1:list[float, float, float], vec2:list[float, float, float])->list[float, float, float]:
        vec1 = list2tuple(vec1)
        vec2 = list2tuple(vec2)
        rec = connect.send_message(f"true<<343<<{vec1}<<{vec2}")
        vec = tuple2list(rec)
        return vec
    
    class funk:
        def get_float(funkexpression:str)->float:
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
        rec = connect.send_message(f"true<<3534")
        vec = tuple2list(rec)
        return vec
