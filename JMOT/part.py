from JMOT import connect
from typing import Literal
import numpy as np

def tuple2array(vec:tuple[float, float, float])->np.ndarray:
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return np.array(vec)

def array2tuple(vec:np.ndarray)->tuple[float, float, float]:
    vec = vec.tolist()
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    vec = tuple(vec)
    return vec


def partname_of_partID(partID:int)->str:
    rec = connect.send_message(f"true<<400<<{partID}")
    return rec[0]
def part_mass(partID:int)->float:
    rec = connect.send_message(f"true<<401<<{partID}")
    return rec[0]
def part_dry_mass(partID:int)->float:
    rec = connect.send_message(f"true<<402<<{partID}")
    return rec[0]
def part_fuel_mass(partID:int)->float:
    rec = connect.send_message(f"true<<403<<{partID}")
    return rec[0]
def is_part_active(partID:int)->bool:
    rec = connect.send_message(f"true<<404<<{partID}")
    return rec[0]
def part_type(partID:int)->str:
    rec = connect.send_message(f"true<<405<<{partID}")
    return rec[0]
def part_position(partID:int)->np.ndarray:
    rec = connect.send_message(f"true<<406<<{partID}")
    vec = tuple2array(rec[0])
    return vec
def part_temperature(partID:int)->float:
    rec = connect.send_message(f"true<<407<<{partID}")
    return rec[0]
def part_drag(partID:int)->float:
    rec = connect.send_message(f"true<<408<<{partID}")
    return rec[0]
def this_part_id(partID=1)->int:
    rec = connect.send_message(f"true<<409<<{partID}")
    return rec[0]
def min_part_id(partID=1)->int:
    rec = connect.send_message(f"true<<410<<{partID}")
    return rec[0]
def max_part_id(partID=1)->int:
    rec = connect.send_message(f"true<<411<<{partID}")
    return rec[0]
def is_part_under_water(partID:int)->float:
    rec = connect.send_message(f"true<<412<<{partID}")
    return rec[0]
def part_loacl_to_eci(partID:int, vector:np.ndarray)->np.ndarray:
    v = array2tuple(vector)
    rec = connect.send_message(f"true<<413<<{partID}<<{v}")
    vec = tuple2array(rec[0])
    return vec
def part_eci_to_local(partID:int, vector:np.ndarray)->np.ndarray:
    v = array2tuple(vector)
    rec = connect.send_message(f"true<<414<<{partID}<<{v}")
    vec = tuple2array(rec[0])
    return vec
def partID_of_partname(part_name:str)->int:
    rec = connect.send_message(f"true<<415<<{part_name}")
    return rec[0]

class control:
    def part_active(part_id:int, part_status:bool):
        ack = connect.send_message(f"false<<9<<{part_id}<<{part_status}")
        connect.verify(ack)

    def part_focuse(part_id:int, part_focuse:bool):
        ack = connect.send_message(f"false<<10<<{part_id}<<{part_focuse}")
        connect.verify(ack)

    def part_name(part_id:int, part_name:str):
        ack = connect.send_message(f"false<<11<<{part_id}<<{part_name}")
        connect.verify(ack)

    def part_explode(part_id:int, part_explode_power:float):
        ack = connect.send_message(f"false<<12<<{part_id}<<{part_explode_power}")
        connect.verify(ack)

    def part_transfer(part_id:int, part_trans:float):
        ack = connect.send_message(f"false<<13<<{part_id}<<{part_trans}")
        connect.verify(ack)