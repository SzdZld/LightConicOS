from JMOT import connect, extra
from typing import Literal
import numpy as np

_PART_SIGNALS = {
    "partname_of_partID": 400,
    "part_mass": 401,
    "part_dry_mass": 402,
    "part_fuel_mass": 403,
    "part_active": 404,
    "part_type": 405,
    "part_position": 406,
    "part_temperature": 407,
    "part_drag": 408,
    "this_part_id": 409,
    "min_part_id": 410,
    "max_part_id": 411,
    "is_part_under_water": 412,
    "partID_of_partname": 415,
    "get_variable": 355
}

def partname_of_partID(partID:int)->str:
    '''Get the name of a part ID.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['partname_of_partID']}<<{partID}")
    return rec[0]
def part_mass(partID:int)->float:
    '''Get the mass of a part ID.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['part_mass']}<<{partID}")
    return rec[0]
def part_dry_mass(partID:int)->float:
    '''Get the dry mass of a part ID.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['part_dry_mass']}<<{partID}")
    return rec[0]
def part_fuel_mass(partID:int)->float:
    '''Get the fuel mass of a part ID.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['part_fuel_mass']}<<{partID}")
    return rec[0]
def is_part_active(partID:int)->bool:
    '''Get the status of whether a part is active.\n
    if active, return True, else return False.'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['part_active']}<<{partID}")
    return rec[0]
def part_type(partID:int)->str:
    '''Get the type of a part ID.\n
    type???
    '''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['part_type']}<<{partID}")
    return rec[0]
def part_position(partID:int)->np.ndarray:
    '''Get the position of a part ID in ECI coordinates.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['part_position']}<<{partID}")
    vec = extra.tuple2array(rec[0])
    return vec
def part_temperature(partID:int)->float:
    '''Get the temperature of a part ID in K.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['part_temperature']}<<{partID}")
    return rec[0]
def part_drag(partID:int)->float:
    '''Get the drag of a part ID in N.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['part_drag']}<<{partID}")
    return rec[0]
def this_part_id(partID=1)->int:
    '''Get the part ID of the part that is currently being called.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['this_part_id']}<<{partID}")
    return rec[0]
def min_part_id(partID=1)->int:
    '''Get the minimum part ID of the current vessel.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['min_part_id']}<<{partID}")
    return rec[0]
def max_part_id(partID=1)->int:
    '''Get the maximum part ID of the current vessel.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['max_part_id']}<<{partID}")
    return rec[0]
def is_part_under_water(partID:int)->float:
    '''Get the status of whether a part is under water.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['is_part_under_water']}<<{partID}")
    return rec[0]
def partID_of_partname(part_name:str)->int:
    '''Get the part ID of a part name.\n'''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['partID_of_partname']}<<{part_name}")
    return rec[0]
def get_variable(part_id:int, variable_name:str)->str:
    '''Get the value of a variable of a part.\n
    i don't know what return when part_id is 0.???
    '''
    rec = connect._send_message(f"true<<{_PART_SIGNALS['get_variable']}<<{part_id}<<{variable_name}")
    return rec[0]