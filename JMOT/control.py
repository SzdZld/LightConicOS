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
<<<<<<< HEAD
        ack = connect.send_message(f"false<<1<<{message}")
        verify(ack)

    def local_log(message:str):
        ack = connect.send_message(f"false<<2<<{message}")
        verify(ack)

    def flight_log(message:str, override:bool):
        ack = connect.send_message(f"false<<3<<{message}<<{override}")
=======
        ack = connect.send_message(f"false<<display<<{message}")
        verify(ack)

    def local_log(message:str):
        ack = connect.send_message(f"false<<lolog<<{message}")
        verify(ack)

    def flight_log(message:str, override:bool):
        ack = connect.send_message(f"false<<fllog<<{message}<<{override}")
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        verify(ack)

class action:
    def active_stage():
<<<<<<< HEAD
        ack = connect.send_message(f"false<<5")
        verify(ack)

    def switch_craft(craft_name:str):
        ack = connect.send_message(f"false<<6<<{craft_name}")
        verify(ack)

    def set_target(target_name:str):
        ack = connect.send_message(f"false<<7<<{target_name}")
        verify(ack)

    def set_ag(active_group:int, status:bool):
        ack = connect.send_message(f"false<<8<<{active_group}<<{status}")
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
        verify(ack)

    class set_part():
        def active(part_id:int, part_status:bool):
<<<<<<< HEAD
            ack = connect.send_message(f"false<<9<<{part_id}<<{part_status}")
            verify(ack)

        def focuse(part_id:int, part_focuse:bool):
            ack = connect.send_message(f"false<<10<<{part_id}<<{part_focuse}")
            verify(ack)

        def name(part_id:int, part_name:str):
            ack = connect.send_message(f"false<<11<<{part_id}<<{part_name}")
            verify(ack)

        def explode(part_id:int, part_explode_power:float):
            ack = connect.send_message(f"false<<12<<{part_id}<<{part_explode_power}")
            verify(ack)

        def transfer(part_id:int, part_trans:float):
            ack = connect.send_message(f"false<<13<<{part_id}<<{part_trans}")
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
            verify(ack)

class control:
    def set_attitude(attitude:Literal["pitch", "yaw", "roll"], value:float):
<<<<<<< HEAD
        ack = connect.send_message(f"false<<20<<{ATTITUDE[attitude]}<<{value}")
        verify(ack)

    def set_throttle(throttle:float):
        ack = connect.send_message(f"false<<21<<{throttle}")
        verify(ack)

    def set_brake(brake:float):
        ack = connect.send_message(f"false<<22<<{brake}")
        verify(ack)

    def set_pitching(value:float):
        ack = connect.send_message(f"false<<23<<{value}")
        verify(ack)

    def set_heading(value:float):
        ack = connect.send_message(f"false<<24<<{value}")
        verify(ack)

    def set_slider(slider:int, slider_value:float):
        ack = connect.send_message(f"false<<25<<{slider}<<{slider_value}")
        verify(ack)

=======
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

>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
    def set_heading_vector(heading:list[float, float, float]):
        tmp = heading[1]
        heading[1] = heading[2]
        heading[2] = tmp
        vec = tuple(heading)
<<<<<<< HEAD
        ack = connect.send_message(f"false<<26<<{vec}")
        verify(ack)

    def set_translate(translate:Literal['forward', 'right', 'up', 'mode'], value:float):
        ack = connect.send_message(f"false<<27<<{TRANSLATE[translate]}<<{value}")
        verify(ack)

    def lock_head_mode(mode:Literal['none', 'prograde', 'retrograde', 'target', 'burnmode', 'current']):
        ack = connect.send_message(f"false<<28<<{HEADMODE[mode]}")
        verify(ack)

def set_variable(part_id:int, variable_name:str, value:all):
    ack = connect.send_message(f"false<<40<<{part_id}<<{variable_name}<<{value}")
=======
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
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3
    verify(ack)

def set_time_mode(time_mode:Literal[-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13]):
    '''
    -1:0.05x\n
    0:pause\n
    1:normal\n
    2:fast(10x)\n
    3:25x\n
    4:100x\n
    5:500x\n
    6:2500x\n
    7:1W x\n
    8:5W x\n
    9:25W x\n
    10:100W x\n
    11:500W x\n
    12:2500W x\n
    13:1Y x
    '''

    ack = connect.send_message(f"false<<51<<{time_mode}")
    verify(ack)

# camera,voice先不做