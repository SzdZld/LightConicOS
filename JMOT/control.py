from JMOT import connect, extra
from typing import Literal
import numpy as np

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
    ack = connect.send_message(f"false<<1<<{message}")
    connect.connect.verify(ack)

def local_log(message:str):
    '''Log a message in the part local log file.\n'''
    ack = connect.send_message(f"false<<2<<{message}")
    connect.connect.verify(ack)

def flight_log(message:str, override:bool):
    '''Log a message in the flight log file.\n
    override:
        if override is True, the message will be overridden. \n
        if override is False, the message will be added to the end of the log file. \n 
    '''
    ack = connect.send_message(f"false<<3<<{message}<<{override}")
    connect.connect.verify(ack)

def active_stage():
    '''Activate the next stage.\n'''
    ack = connect.send_message(f"false<<5")
    connect.verify(ack)

def switch_craft(craft_id:int):
    '''Switch to a different craft.\n'''
    ack = connect.send_message(f"false<<6<<{craft_id}")
    connect.verify(ack)

def set_target(target_name:str):
    '''Set the target of the vessel or planet.\n'''
    ack = connect.send_message(f"false<<7<<{target_name}")
    connect.verify(ack)

def set_ag(active_group:int, status:bool):
    '''Set the status of an action group.\n'''
    ack = connect.send_message(f"false<<8<<{active_group}<<{status}")
    connect.verify(ack)

def set_attitude(attitude:Literal["pitch", "yaw", "roll"], value:float):
    '''Set the value of an attitude.\n
    attitude:
        pitch,yaw,roll \n
    \n'''
    ack = connect.send_message(f"false<<20<<{ATTITUDE[attitude]}<<{value}")
    connect.verify(ack)

def set_throttle(throttle:float):
    '''Set the throttle value.\n'''
    ack = connect.send_message(f"false<<21<<{throttle}")
    connect.verify(ack)

def set_brake(brake:float):
    '''Set the brake value.\n'''
    ack = connect.send_message(f"false<<22<<{brake}")
    connect.verify(ack)

def set_pitching(pitching:float):
    '''Set the pitching value.\n'''
    ack = connect.send_message(f"false<<23<<{pitching}")
    connect.verify(ack)

def set_heading(heading:float):
    '''Set the heading value.\n'''
    ack = connect.send_message(f"false<<24<<{heading}")
    connect.verify(ack)

def set_slider(slider:int, slider_value:float):
    '''Set the value of a slider.\n'''
    ack = connect.send_message(f"false<<25<<{slider}<<{slider_value}")
    connect.verify(ack)

def set_heading_vector(heading:np.ndarray):
    '''Set the heading vector in ECI coordinates.\n'''
    vec = extra.array2tuple(heading)
    ack = connect.send_message(f"false<<26<<{vec}")
    connect.verify(ack)

def set_translate(translate:Literal['forward', 'right', 'up', 'mode'], value:float):
    '''Set the value of a translate.\n
    translate:\n
        forward:-1(back)-1(forward) \n
        'right':-1(left)-1(right) \n
        'up':-1(down)-1(up) \n
        'mode':0(attitude mode) or 1(translate mode) \n
    '''
    ack = connect.send_message(f"false<<27<<{TRANSLATE[translate]}<<{value}")
    connect.verify(ack)

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
    ack = connect.send_message(f"false<<28<<{HEADMODE[mode]}")
    connect.verify(ack)

def set_variable(part_id:int, variable_name:str, value:all):
    '''Set the value of a variable in a part:\n
        part_id:the part ID of the part\n
        variable_name:the name of the variable in the part\n
        value:the value of the variable\n
    '''
    ack = connect.send_message(f"false<<40<<{part_id}<<{variable_name}<<{value}")
    connect.verify(ack)

def part_active(part_id:int, part_status:bool):
    '''Set the status of a part.\n'''
    ack = connect.send_message(f"false<<9<<{part_id}<<{part_status}")
    connect.verify(ack)

def part_focuse(part_id:int, part_focuse:bool):
    '''Set the camera focus of a part.\n'''
    ack = connect.send_message(f"false<<10<<{part_id}<<{part_focuse}")
    connect.verify(ack)

def part_name(part_id:int, part_name:str):
    '''Set the name of a part.\n'''
    ack = connect.send_message(f"false<<11<<{part_id}<<{part_name}")
    connect.verify(ack)

def part_explode(part_id:int, part_explode_power:float):
    '''Explode a part.\n
    part_explode_power:the power of the explosion,\n
        0 means no explosion but drop down, 1 means full explosion.\n
    '''
    ack = connect.send_message(f"false<<12<<{part_id}<<{part_explode_power}")
    connect.verify(ack)

def part_transfer(part_id:int, part_trans:float):
    '''Transfer a part.\n
    part_trans:the transfer value,\n
        <0 means exhuast\n
        0 means no transfer\n
        >0 means fill.\n
    '''
    ack = connect.send_message(f"false<<13<<{part_id}<<{part_trans}")
    connect.verify(ack)
    