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
    def display(message:str, socket):
        ack = connect.send_message(f"false<<display<<{message}", socket)
        verify(ack)

    def local_log(message:str, socket):
        ack = connect.send_message(f"false<<lolog<<{message}", socket)
        verify(ack)

    def flight_log(message:str, override:bool, socket):
        ack = connect.send_message(f"false<<fllog<<{message}<<{override}", socket)
        verify(ack)

class action:
    def active_stage(socket):
        ack = connect.send_message(f"false<<actstg", socket)
        verify(ack)

    def switch_craft(craft_name:str, socket):
        ack = connect.send_message(f"false<<swcft<<{craft_name}", socket)
        verify(ack)

    def set_target(target_name:str, socket):
        ack = connect.send_message(f"false<<settarget<<{target_name}", socket)
        verify(ack)

    def set_ag(active_group:int, status:bool, socket):
        ack = connect.send_message(f"false<<setag<<{active_group}<<{status}", socket)
        verify(ack)

    class set_part():
        def active(part_id:int, part_status:bool, socket):
            ack = connect.send_message(f"false<<partact<<{part_id}<<{part_status}", socket)
            verify(ack)

        def active(part_id:int, part_focuse:bool, socket):
            ack = connect.send_message(f"false<<partfoc<<{part_id}<<{part_focuse}", socket)
            verify(ack)

        def name(part_id:int, part_name:str, socket):
            ack = connect.send_message(f"false<<setpartname<<{part_id}<<{part_name}", socket)
            verify(ack)

        def explode(part_id:int, part_explode_power:float, socket):
            ack = connect.send_message(f"false<<partexp<<{part_id}<<{part_explode_power}", socket)
            verify(ack)

        def transfer(part_id:int, part_trans:float, socket):
            ack = connect.send_message(f"false<<partexp<<{part_id}<<{part_trans}", socket)
            verify(ack)

class control:
    def set_attitude(attitude:Literal["pitch", "yaw", "roll"], value:float, socket):
        ack = connect.send_message(f"false<<setatt<<{ATTITUDE[attitude]}<<{value}", socket)
        verify(ack)

    def set_throttle_brake(throttle:float, socket):
        ack = connect.send_message(f"false<<setlvr<<{throttle}", socket)
        verify(ack)

    def set_pitch_heading(set_value:Literal["pitch", "heading"], value:float, socket):
        ack = connect.send_message(f"false<<sethead<<{set_value}<<{value}", socket)
        verify(ack)

    def set_slider(slider:int, slider_value:float, socket):
        ack = connect.send_message(f"false<<setslider<<{slider}<<{slider_value}", socket)
        verify(ack)

    def set_heading_vector(heading:list[float, float, float], socket):
        tmp = heading[1]
        heading[1] = heading[2]
        heading[2] = tmp
        vec = tuple(heading)
        ack = connect.send_message(f"false<<setheadvec<<{vec}", socket)
        verify(ack)

    def set_translate(translate:Literal['forward', 'right', 'up', 'mode'], value:float, socket):
        ack = connect.send_message(f"false<<settsl<<{TRANSLATE[translate]}<<{value}", socket)
        verify(ack)

    def lock_head_mode(mode:Literal['none', 'prograde', 'retrograde', 'target', 'burnmode', 'current'], socket):
        ack = connect.send_message(f"false<<lockhead<<{HEADMODE[mode]}", socket)
        verify(ack)

def set_variable(part_id:int, variable_name:str, value:all, socket):
    ack = connect.send_message(f"false<<setvar<<{part_id}<<{variable_name}<<{value}", socket)
    verify(ack)

def set_time_mode(time_mode:Literal['timewarp1', 'timewarp3', 'timewarp5', 'timewarp7', 'timewarp9', 'normal']):
    # 和camera,voice先不做
    pass