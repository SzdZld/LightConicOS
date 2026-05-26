from JMOT import connect, extra
from typing import Literal
import numpy as np

_CONTROL_SIGNAL = {
    'display' : 1,
    'local_log' : 2,
    'flight_log' : 3,
    'active_stage' : 5,
    'switch_craft' : 6,
    'set_target' : 7,
    'set_ag' : 8,
    'set_attitude' : 20,
    'set_throttle' : 21,
    'set_brake' : 22,
    'set_pitching' : 23,
    'set_heading' : 24,
    'set_slider' : 25,
    'set_heading_vector' : 26,
    'set_translate' : 27,
    'lock_head_mode' : 28,
    'set_variable' : 41,
    'set_variable_list' : 42,
    'set_part_active' : 9,
    'set_part_focuse' : 10,
    'set_part_name' : 11,
    'set_part_explode' : 12,
    'set_part_transfer' : 13
}

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


def display(message:str):
    '''Display a message on the screen.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['display']}<<{message}")
    connect._verify(ack)

def local_log(message:str):
    '''Log a message in the part local log file.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['local_log']}<<{message}")
    connect._verify(ack)

def flight_log(message:str, override:bool):
    '''Log a message in the flight log file.\n
    override:
        if override is True, the message will be overridden. \n
        if override is False, the message will be added to the end of the log file. \n 
    '''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['flight_log']}<<{message}<<{override}")
    connect._verify(ack)

def active_stage():
    '''Activate the next stage.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['active_stage']}")
    connect._verify(ack)

def switch_craft(craft_id:int):
    '''Switch to a different craft.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['switch_craft']}<<{craft_id}")
    connect._verify(ack)

def set_target(target_name:str):
    '''Set the target of the vessel or planet.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_target']}<<{target_name}")
    connect._verify(ack)

def set_ag(active_group:int, status:bool):
    '''Set the status of an action group.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_ag']}<<{active_group}<<{status}")
    connect._verify(ack)

def set_attitude(attitude:Literal["pitch", "yaw", "roll"], value:float):
    '''Set the value of an attitude.\n
    attitude:
        pitch,yaw,roll \n
    \n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_attitude']}<<{ATTITUDE[attitude]}<<{value}")
    connect._verify(ack)

def set_throttle(throttle:float):
    '''Set the throttle value.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_throttle']}<<{throttle}")
    connect._verify(ack)

def set_brake(brake:float):
    '''Set the brake value.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_brake']}<<{brake}")
    connect._verify(ack)

def set_pitching(pitching:float):
    '''Set the pitching value.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_pitching']}<<{pitching}")
    connect._verify(ack)

def set_heading(heading:float):
    '''Set the heading value.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_heading']}<<{heading}")
    connect._verify(ack)

def set_slider(slider:int, slider_value:float):
    '''Set the value of a slider.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_slider']}<<{slider}<<{slider_value}")
    connect._verify(ack)

def set_heading_vector(heading:np.ndarray):
    '''Set the heading vector in ECI coordinates.\n'''
    vec = extra.array2tuple(heading)
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_heading_vector']}<<{vec}")
    connect._verify(ack)

def set_translate(translate:Literal['forward', 'right', 'up', 'mode'], value:float):
    '''Set the value of a translate.\n
    translate:\n
        forward:-1(back)-1(forward) \n
        'right':-1(left)-1(right) \n
        'up':-1(down)-1(up) \n
        'mode':0(attitude mode) or 1(translate mode) \n
    '''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_translate']}<<{TRANSLATE[translate]}<<{value}")
    connect._verify(ack)

def lock_head_mode(mode:Literal['none', 'prograde', 'retrograde', 'target', 'burnmode', 'current']):
    '''Lock the head mode of the vessel.\n
    mode:\n
        none:no head mode\n
        prograde:lock to prograde\n
        retrograde:lock to retrograde\n
        target:lock to target\n
        burnmode:lock to burn mode\n
        current:lock to current direction\n
    '''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['lock_head_mode']}<<{HEADMODE[mode]}")
    connect._verify(ack)

def set_variable(part_id:int, variable_name:str, value:all):
    '''Set the value of a variable in a part:\n
        part_id:the part ID of the part\n
        variable_name:the name of the variable in the part\n
        value:the value of the variable\n
    '''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_variable']}<<{part_id}<<{variable_name}<<{value}")
    connect._verify(ack)

def set_variable_list(part_id: int, list_variable_name: str, value_list: int|float|str|bool):
    '''Set the value of a list variable in a part.\n
       part_id:the part ID of the part\n   
       list_variable_name:the name of the list variable in the part\n
       value_list:the list of values of the variable\n
    '''
    safe_value_list = [str(item) for item in value_list]
    
    ack = connect._send_message(
        f"false<<{_CONTROL_SIGNAL['set_variable_list']}<<{part_id}<<{list_variable_name}<<{safe_value_list}"
    )
    connect._verify(ack)

def set_part_active(part_id:int, part_status:bool):
    '''Set the status of a part.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_part_active']}<<{part_id}<<{part_status}")
    connect._verify(ack)

def set_part_focuse(part_id:int, part_focuse:bool):
    '''Set the camera focus of a part.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_part_focuse']}<<{part_id}<<{part_focuse}")
    connect._verify(ack)

def set_part_name(part_id:int, part_name:str):
    '''Set the name of a part.\n'''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_part_name']}<<{part_id}<<{part_name}")
    connect._verify(ack)

def set_part_explode(part_id:int, part_explode_power:float):
    '''Explode a part.\n
    part_explode_power:the power of the explosion,\n
        0 means no explosion but drop down, 1 means full explosion.\n
    '''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_part_explode']}<<{part_id}<<{part_explode_power}")
    connect._verify(ack)

def set_part_transfer(part_id:int, part_trans:float):
    '''Transfer a part.\n
    part_trans:the transfer value,\n
        <0 means exhuast\n
        0 means no transfer\n
        >0 means fill.\n
    '''
    ack = connect._send_message(f"false<<{_CONTROL_SIGNAL['set_part_transfer']}<<{part_id}<<{part_trans}")
    connect._verify(ack)
    