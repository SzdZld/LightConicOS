from JMOT import connect, extra
from typing import Literal
import numpy as np

def partname_of_partID(partID:int)->str:
    '''Get the name of a part ID.\n'''
    rec = connect.send_message(f"true<<400<<{partID}")
    return rec[0]
def part_mass(partID:int)->float:
    '''Get the mass of a part ID.\n'''
    rec = connect.send_message(f"true<<401<<{partID}")
    return rec[0]
def part_dry_mass(partID:int)->float:
    '''Get the dry mass of a part ID.\n'''
    rec = connect.send_message(f"true<<402<<{partID}")
    return rec[0]
def part_fuel_mass(partID:int)->float:
    '''Get the fuel mass of a part ID.\n'''
    rec = connect.send_message(f"true<<403<<{partID}")
    return rec[0]
def is_part_active(partID:int)->bool:
    '''Get the status of whether a part is active.\n
    if active, return True, else return False.'''
    rec = connect.send_message(f"true<<404<<{partID}")
    return rec[0]
def part_type(partID:int)->str:
    '''Get the type of a part ID.\n
    type???
    '''
    rec = connect.send_message(f"true<<405<<{partID}")
    return rec[0]
def part_position(partID:int)->np.ndarray:
    '''Get the position of a part ID in ECI coordinates.\n'''
    rec = connect.send_message(f"true<<406<<{partID}")
    vec = extra.tuple2array(rec[0])
    return vec
def part_temperature(partID:int)->float:
    '''Get the temperature of a part ID in K.\n'''
    rec = connect.send_message(f"true<<407<<{partID}")
    return rec[0]
def part_drag(partID:int)->float:
    '''Get the drag of a part ID in N.\n'''
    rec = connect.send_message(f"true<<408<<{partID}")
    return rec[0]
def this_part_id(partID=1)->int:
    '''Get the part ID of the part that is currently being called.\n'''
    rec = connect.send_message(f"true<<409<<{partID}")
    return rec[0]
def min_part_id(partID=1)->int:
    '''Get the minimum part ID of the current vessel.\n'''
    rec = connect.send_message(f"true<<410<<{partID}")
    return rec[0]
def max_part_id(partID=1)->int:
    '''Get the maximum part ID of the current vessel.\n'''
    rec = connect.send_message(f"true<<411<<{partID}")
    return rec[0]
def is_part_under_water(partID:int)->float:
    '''Get the status of whether a part is under water.\n'''
    rec = connect.send_message(f"true<<412<<{partID}")
    return rec[0]
def partID_of_partname(part_name:str)->int:
    '''Get the part ID of a part name.\n'''
    rec = connect.send_message(f"true<<415<<{part_name}")
    return rec[0]
def get_variable(part_id:int, variable_name:str)->str:
    '''Get the value of a variable of a part.\n
    i don't know what return when part_id is 0.???
    '''
    rec = connect.send_message(f"true<<355<<{part_id}<<{variable_name}")
    return rec[0]