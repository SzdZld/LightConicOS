from JMOT import connect
from typing import Literal


def verify(response):
        if response[0]:
            pass
        else:
            print("send error")

ATTITUDE = {
    "pitch":1,
    "yaw":2,
    "roll":3
}

TRANSLATE = {
    'forward' : 1,
    'right' : 2,
    'up' : 3,
    'mode' : 4
}

HEADMODE = {
    'none' : 1,
    'prograde' : 2, 
    'retrograde' : 3, 
    'target' : 4, 
    'burnmode' : 5, 
    'current' : 6
}

class display:
    def display(message:str):
        ack = connect.send_message(f"false<<display<<{message}")
        verify(ack)

    def local_log(message:str):
        ack = connect.send_message(f"false<<lolog<<{message}")
        verify(ack)

    def flight_log(message:str, override:bool):
        ack = connect.send_message(f"false<<fllog<<{message}<<{override}")
        verify(ack)

class action:
    def active_stage():
        ack = connect.send_message(f"false<<actstg")
        verify(ack)

    def switch_craft(craft_name:str):
        ack = connect.send_message(f"false<<swcft<<{craft_name}")
        verify(ack)

    def set_target(target_name:str):
        ack = connect.send_message(f"false<<settarget<<{target_name}")
        verify(ack)

    def set_ag(active_group:int, status:bool):
        ack = connect.send_message(f"false<<setag<<{active_group}<<{status}")
        verify(ack)

    class set_part():
        def active(part_id:int, part_status:bool):
            ack = connect.send_message(f"false<<partact<<{part_id}<<{part_status}")
            verify(ack)

        def active(part_id:int, part_focuse:bool):
            ack = connect.send_message(f"false<<partfoc<<{part_id}<<{part_focuse}")
            verify(ack)

        def name(part_id:int, part_name:str):
            ack = connect.send_message(f"false<<setpartname<<{part_id}<<{part_name}")
            verify(ack)

        def explode(part_id:int, part_explode_power:float):
            ack = connect.send_message(f"false<<partexp<<{part_id}<<{part_explode_power}")
            verify(ack)

        def transfer(part_id:int, part_trans:float):
            ack = connect.send_message(f"false<<partexp<<{part_id}<<{part_trans}")
            verify(ack)

class control:
    def set_attitude(attitude:Literal["pitch", "yaw", "roll"], value:float):
        ack = connect.send_message(f"false<<setatt<<{ATTITUDE[attitude]}<<{value}")
        verify(ack)

    def set_throttle(throttle:float):
        ack = connect.send_message(f"false<<setthr<<{throttle}")
        verify(ack)

    def set_brake(brake:float):
        ack = connect.send_message(f"false<<setbrk<<{brake}")
        verify(ack)

    def set_pitch_heading(set_value:Literal["pitch", "heading"], value:float):
        ack = connect.send_message(f"false<<sethead<<{set_value}<<{value}")
        verify(ack)

    def set_slider(slider:int, slider_value:float):
        ack = connect.send_message(f"false<<setslider<<{slider}<<{slider_value}")
        verify(ack)

    def set_heading_vector(heading:list[float, float, float]):
        tmp = heading[1]
        heading[1] = heading[2]
        heading[2] = tmp
        vec = tuple(heading)
        ack = connect.send_message(f"false<<setheadvec<<{vec}")
        verify(ack)

    def set_translate(translate:Literal['forward', 'right', 'up', 'mode'], value:float):
        ack = connect.send_message(f"false<<settsl<<{TRANSLATE[translate]}<<{value}")
        verify(ack)

    def lock_head_mode(mode:Literal['none', 'prograde', 'retrograde', 'target', 'burnmode', 'current']):
        ack = connect.send_message(f"false<<lockhead<<{HEADMODE[mode]}")
        verify(ack)

def set_variable(part_id:int, variable_name:str, value:all):
    ack = connect.send_message(f"false<<setvar<<{part_id}<<{variable_name}<<{value}")
    verify(ack)

def set_time_mode(time_mode:Literal['timewarp1', 'timewarp3', 'timewarp5', 'timewarp7', 'timewarp9', 'normal']):
    # 和camera,voice先不做
    pass