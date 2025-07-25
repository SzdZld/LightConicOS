from JMOT import connect
from typing import Literal

def tuple2list(vec:tuple[float, float, float])->list[float, float, float]:
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return vec

class info():
    def get_name(socket)->str:
        rec = connect.send_message(f"true<<79", socket)
        return rec[0]
    def get_name_of_target(socket)->str:
        rec = connect.send_message(f"true<<81", socket)
        return rec[0]
    def name_of_craftID(craft_ID:int, socket)->str:
        rec = connect.send_message(f"true<<104<<{craft_ID}", socket)
        return rec[0]
    def part_count_of_craftID(craft_ID:int, socket)->int:
        rec = connect.send_message(f"true<<105<<{craft_ID}", socket)
        return rec[0]
    def craftID_of_craftname(craft_name:str, socket)->int:
        rec = connect.send_message(f"true<<105<<{craft_name}", socket)
        return rec[0]

class time():
    def time_since_launch(socket)->float:
        rec = connect.send_message(f"true<<75", socket)
        return rec[0]
    def total_time(socket)->float:
        rec = connect.send_message(f"true<<76", socket)
        return rec[0]

class performance():
    def get_battery(socket)->float:
        rec = connect.send_message(f"true<<8", socket)
        return rec[0]
    def get_stage_fuel(socket)->float:
        rec = connect.send_message(f"true<<9", socket)
        return rec[0]
    def get_mono_fuel(socket)->float:
        rec = connect.send_message(f"true<<10", socket)
        return rec[0]
    def get_engine_thrust(socket)->float:
        rec = connect.send_message(f"true<<19", socket)
        return rec[0]
    def get_mass(socket)->float:
        rec = connect.send_message(f"true<<20", socket)
        return rec[0]
    def get_max_engine_thrust(socket)->float:
        rec = connect.send_message(f"true<<23", socket)
        return rec[0]
    def get_TWR(socket)->float:
        rec = connect.send_message(f"true<<24", socket)
        return rec[0]
    def get_ISP(socket)->float:
        rec = connect.send_message(f"true<<25", socket)
        return rec[0]
    def get_stage_delta_v(socket)->float:
        rec = connect.send_message(f"true<<26", socket)
        return rec[0]
    def get_stage_burn_time(socket)->float:
        rec = connect.send_message(f"true<<27", socket)
        return rec[0]
    def get_craft_mass(craft_ID:int, socket)->float:
        rec = connect.send_message(f"true<<103<<{craft_ID}", socket)
        return rec[0]

class position():
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

class attitude():
    def craft_heading(socket)->float:
        rec = connect.send_message(f"true<<30", socket)
        return rec
    def craft_pitching(socket)->float:
        rec = connect.send_message(f"true<<31", socket)
        return rec
    def craft_autopilot_heading(socket)->float:
        rec = connect.send_message(f"true<<32", socket)
        return rec
    def craft_autopilot_pitching(socket)->float:
        rec = connect.send_message(f"true<<33", socket)
        return rec
    def craft_bank_angle(socket)->float:
        rec = connect.send_message(f"true<<34", socket)
        return rec
    def craft_AOA(socket)->float:
        rec = connect.send_message(f"true<<35", socket)
        return rec
    def craft_side_slip(socket)->float:
        rec = connect.send_message(f"true<<36", socket)
        return rec
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

class velocity():
    pass
class orbit():
    pass
class input():
    pass
class misc():
    pass