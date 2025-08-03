from JMOT import connect
from typing import Literal

def tuple2list(vec:tuple[float, float, float])->list[float, float, float]:
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return vec


class info:
    def mass(planet:str)->float:
        rec = connect.send_message(f"true<<100<<{planet}")
        return rec[0]
    def radius(planet:str)->float:
        rec = connect.send_message(f"true<<101<<{planet}")
        return rec[0]
    def is_solid_ground(planet:str)->bool:
        rec = connect.send_message(f"true<<102<<{planet}")
        return rec[0]
    def SOI_radius(planet:str)->float:
        rec = connect.send_message(f"true<<103<<{planet}")
        return rec[0]
    def len_of_day(planet:str)->float:
        rec = connect.send_message(f"true<<104<<{planet}")
        return rec[0]
    def len_of_year(planet:str)->float:
        rec = connect.send_message(f"true<<105<<{planet}")
        return rec[0]
    def name()->str:
        rec = connect.send_message(f"true<<106")
        return rec[0]
    def target_name()->str:
        rec = connect.send_message(f"true<<107")
        return rec[0]
    def parent(planet:str)->str:
        rec = connect.send_message(f"true<<108<<{planet}")
        return rec[0]
    def child_planets_list(planet:str)->list:
        rec = connect.send_message(f"true<<109<<{planet}")
        return rec
    def craft_list(planet:str)->list:
        rec = connect.send_message(f"true<<110<<{planet}")
        return rec
    def craft_ID_list(planet:str)->list:
        rec = connect.send_message(f"true<<111<<{planet}")
        return rec
    def structure_list(planet:str)->list:
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
    def solar_position(planet:str)->list[float, float, float]:
        rec = connect.send_message(f"true<<150<<{planet}")
        vec = tuple2list(rec)
        return vec
    def velocity(planet:str)->list[float, float, float]:
        rec = connect.send_message(f"true<<151<<{planet}")
        vec = tuple2list(rec)
        return vec
    def apoapsis_position(planet:str)->list[float, float, float]:
        rec = connect.send_message(f"true<<152<<{planet}")
        vec = tuple2list(rec)
        return vec
    def periapsis_position(planet:str)->list[float, float, float]:
        rec = connect.send_message(f"true<<153<<{planet}")
        vec = tuple2list(rec)
        return vec
    def period(planet:str)->float:
        rec = connect.send_message(f"true<<154<<{planet}")
        return rec[0]
    def apoapsis_time(planet:str)->float:
        rec = connect.send_message(f"true<<155<<{planet}")
        return rec[0]
    def periapsis_time(planet:str)->float:
        rec = connect.send_message(f"true<<156<<{planet}")
        return rec[0]
    def inclination(planet:str)->float:
        rec = connect.send_message(f"true<<157<<{planet}")
        return rec[0]
    def eccentricity(planet:str)->float:
        rec = connect.send_message(f"true<<158<<{planet}")
        return rec[0]
    def mean_anomaly(planet:str)->float:
        rec = connect.send_message(f"true<<159<<{planet}")
        return rec[0]
    def mean_motion(planet:str)->float:
        rec = connect.send_message(f"true<<160<<{planet}")
        return rec[0]
    def periapsis_argument(planet:str)->float:
        rec = connect.send_message(f"true<<161<<{planet}")
        return rec[0]
    def right_ascension(planet:str)->float:
        rec = connect.send_message(f"true<<162<<{planet}")
        return rec[0]
    def true_anomaly(planet:str)->float:
        rec = connect.send_message(f"true<<163<<{planet}")
        return rec[0]
    def SMA(planet:str)->float:
        rec = connect.send_message(f"true<<164<<{planet}")
        return rec[0]
