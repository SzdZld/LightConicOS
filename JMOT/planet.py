from JMOT import connect
from typing import Literal
import numpy as np

def tuple2array(vec:tuple[float, float, float])->np.ndarray:
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return np.array(vec)


class info:
    def planet_mass(planet:str)->float:
        rec = connect.send_message(f"true<<100<<{planet}")
        return rec[0]
    def planet_radius(planet:str)->float:
        rec = connect.send_message(f"true<<101<<{planet}")
        return rec[0]
    def is_solid_ground(planet:str)->bool:
        rec = connect.send_message(f"true<<102<<{planet}")
        return rec[0]
    def planet_SOI_radius(planet:str)->float:
        rec = connect.send_message(f"true<<103<<{planet}")
        return rec[0]
    def planet_len_of_day(planet:str)->float:
        rec = connect.send_message(f"true<<104<<{planet}")
        return rec[0]
    def planet_len_of_year(planet:str)->float:
        rec = connect.send_message(f"true<<105<<{planet}")
        return rec[0]
    def name()->str:
        rec = connect.send_message(f"true<<106")
        return rec[0]
    def target_name()->str:
        rec = connect.send_message(f"true<<107")
        return rec[0]
    def planet_parent(planet:str)->str:
        rec = connect.send_message(f"true<<108<<{planet}")
        return rec[0]
    def planet_child_list(planet:str)->list:
        rec = connect.send_message(f"true<<109<<{planet}")
        return rec
    def planet_craft_list(planet:str)->list:
        rec = connect.send_message(f"true<<110<<{planet}")
        return rec
    def planet_craft_ID_list(planet:str)->list:
        rec = connect.send_message(f"true<<111<<{planet}")
        return rec
    def planet_structure_list(planet:str)->list:
        rec = connect.send_message(f"true<<112<<{planet}")
        return rec

class atmosphere:
    def air_desity()->float:
        rec = connect.send_message(f"true<<130")
        return rec[0]
    def air_pressure()->float:
        rec = connect.send_message(f"true<<131")
        return rec[0]
    def speed_of_sound()->float:
        rec = connect.send_message(f"true<<132")
        return rec[0]
    def temperature()->float:
        rec = connect.send_message(f"true<<133")
        return rec[0]
    def atmosphere_air_desity(planet:str)->float:
        rec = connect.send_message(f"true<<134{planet}")
        return rec[0]
    def atmosphere_height(planet:str)->float:
        rec = connect.send_message(f"true<<135{planet}")
        return rec[0]
    def atmosphere_fade_out(planet:str)->float:
        rec = connect.send_message(f"true<<136<<{planet}")
        return rec[0]

class orbit:
    def planet_solar_position(planet:str)->np.ndarray:
        rec = connect.send_message(f"true<<150<<{planet}")
        vec = tuple2array(rec)
        return vec
    def planet_velocity(planet:str)->np.ndarray:
        rec = connect.send_message(f"true<<151<<{planet}")
        vec = tuple2array(rec)
        return vec
    def planet_apoapsis_position(planet:str)->np.ndarray:
        rec = connect.send_message(f"true<<152<<{planet}")
        vec = tuple2array(rec)
        return vec
    def planet_periapsis_position(planet:str)->np.ndarray:
        rec = connect.send_message(f"true<<153<<{planet}")
        vec = tuple2array(rec)
        return vec
    def planet_period(planet:str)->float:
        rec = connect.send_message(f"true<<154<<{planet}")
        return rec[0]
    def planet_apoapsis_time(planet:str)->float:
        rec = connect.send_message(f"true<<155<<{planet}")
        return rec[0]
    def planet_periapsis_time(planet:str)->float:
        rec = connect.send_message(f"true<<156<<{planet}")
        return rec[0]
    def planet_inclination(planet:str)->float:
        rec = connect.send_message(f"true<<157<<{planet}")
        return rec[0]
    def planet_eccentricity(planet:str)->float:
        rec = connect.send_message(f"true<<158<<{planet}")
        return rec[0]
    def planet_mean_anomaly(planet:str)->float:
        rec = connect.send_message(f"true<<159<<{planet}")
        return rec[0]
    def planet_mean_motion(planet:str)->float:
        rec = connect.send_message(f"true<<160<<{planet}")
        return rec[0]
    def planet_periapsis_argument(planet:str)->float:
        rec = connect.send_message(f"true<<161<<{planet}")
        return rec[0]
    def planet_right_ascension(planet:str)->float:
        rec = connect.send_message(f"true<<162<<{planet}")
        return rec[0]
    def planet_true_anomaly(planet:str)->float:
        rec = connect.send_message(f"true<<163<<{planet}")
        return rec[0]
    def planet_SMA(planet:str)->float:
        rec = connect.send_message(f"true<<164<<{planet}")
        return rec[0]
