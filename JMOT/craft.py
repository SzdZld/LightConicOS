from JMOT import connect
from typing import Literal

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
        pass
    def get_stage_fuel(socket)->float:
        pass
    def get_mono_fuel(socket)->float:
        pass
    def get_engine_thrust(socket)->float:
        pass
    def get_mass(socket)->float:
        pass
    def get_max_engine_thrust(socket)->float:
        pass
    def get_TWR(socket)->float:
        pass
    def get_ISP(socket)->float:
        pass
    def get_stage_delta_v(socket)->float:
        pass
    def get_stage_burn_time(socket)->float:
        pass
    def get_craft_mass(craft_ID:int, socket)->float:
        pass
    
class nav():
    pass
class velocity():
    pass
class orbit():
    pass
class input():
    pass
class misc():
    pass