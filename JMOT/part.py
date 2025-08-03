from JMOT import connect
from typing import Literal

def tuple2list(vec:tuple[float, float, float])->list[float, float, float]:
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return vec

def list2tuple(vec:list[float, float, float])->tuple[float, float, float]:
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    vec = tuple(vec)
    return vec


def partname_of_partID(partID:int)->str:
    rec = connect.send_message(f"true<<400<<{partID}")
    return rec[0]
def mass(partID:int)->float:
    rec = connect.send_message(f"true<<401<<{partID}")
    return rec[0]
def dry_mass(partID:int)->float:
    rec = connect.send_message(f"true<<402<<{partID}")
    return rec[0]
def fuel_mass(partID:int)->float:
    rec = connect.send_message(f"true<<403<<{partID}")
    return rec[0]
def is_acitve(partID:int)->bool:
    rec = connect.send_message(f"true<<404<<{partID}")
    return rec[0]
def part_type(partID:int)->str:
    rec = connect.send_message(f"true<<405<<{partID}")
    return rec[0]
def position(partID:int)->list[float, float, float]:
    rec = connect.send_message(f"true<<406<<{partID}")
    vec = tuple2list(rec[0])
    return vec
def temperature(partID:int)->float:
    rec = connect.send_message(f"true<<407<<{partID}")
    return rec[0]
def drag(partID:int)->float:
    rec = connect.send_message(f"true<<408<<{partID}")
    return rec[0]
def this_part_id(partID=0)->int:
    rec = connect.send_message(f"true<<409<<{partID}")
    return rec[0]
def min_part_id(partID=0)->int:
    rec = connect.send_message(f"true<<410<<{partID}")
    return rec[0]
def max_part_id(partID=0)->int:
    rec = connect.send_message(f"true<<411<<{partID}")
    return rec[0]
def under_water(partID:int)->float:
    rec = connect.send_message(f"true<<412<<{partID}")
    return rec[0]
def part_loacl_to_eci(partID:int, vector:list[float, float, float])->list[float, float, float]:
    v = list2tuple(vector)
    rec = connect.send_message(f"true<<413<<{partID}<<{v}")
    vec = tuple2list(rec[0])
    return vec
def part_eci_to_local(partID:int, vector:list[float, float, float])->list[float, float, float]:
    v = list2tuple(vector)
    rec = connect.send_message(f"true<<414<<{partID}<<{v}")
    vec = tuple2list(rec[0])
    return vec
def partID_of_partname(part_name:str)->int:
    rec = connect.send_message(f"true<<415<<{part_name}")
    return rec[0]