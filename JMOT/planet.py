from JMOT import connect, extra
from typing import Literal
import numpy as np


class info:
    def planet_mass(planet:str)->float:
        '''Get the mass of a planet in kg.\n'''
        rec = connect.send_message(f"true<<100<<{planet}")
        return rec[0]
    def planet_radius(planet:str)->float:
        '''Get the radius of a planet in meters.\n'''
        rec = connect.send_message(f"true<<101<<{planet}")
        return rec[0]
    def is_solid_ground(planet:str)->bool:
        '''Get the status of whether the surface of a planet is solid.\n
        if solid, return True, else return False.'''
        rec = connect.send_message(f"true<<102<<{planet}")
        return rec[0]
    def planet_SOI_radius(planet:str)->float:
        '''Get the radius of the sphere of influence of a planet in meters.\n'''
        rec = connect.send_message(f"true<<103<<{planet}")
        return rec[0]
    def planet_len_of_day(planet:str)->float:
        '''Get the length of a day on a planet in seconds.\n'''
        rec = connect.send_message(f"true<<104<<{planet}")
        return rec[0]
    def planet_len_of_year(planet:str)->float:
        '''Get the length of a year on a planet in seconds.\n'''
        rec = connect.send_message(f"true<<105<<{planet}")
        return rec[0]
    def planet_name_local()->str:
        '''Get the name of the current vessel's main celestial body.'''
        rec = connect.send_message(f"true<<106")
        return rec[0]
    def target_planet()->str:
        '''Get the name of the current vessel's target celestial body.'''
        rec = connect.send_message(f"true<<107")
        return rec[0]
    def planet_parent(planet:str)->str:
        '''Get the name of the parent body of a planet.\n'''
        rec = connect.send_message(f"true<<108<<{planet}")
        return rec[0]
    def planet_child_list(planet:str)->list:
        '''Get the list of child bodies of a planet.'''
        rec = connect.send_message(f"true<<109<<{planet}")
        return rec
    def planet_craft_list(planet:str)->list:
        '''Get the list of craft name in orbit around a planet.'''
        rec = connect.send_message(f"true<<110<<{planet}")
        return rec
    def planet_craft_ID_list(planet:str)->list:
        '''Get the list of craft ID in orbit around a planet.'''
        rec = connect.send_message(f"true<<111<<{planet}")
        return rec
    def planet_structure_list(planet:str)->list:
        '''Get the list of structures on a planet.'''
        rec = connect.send_message(f"true<<112<<{planet}")
        return rec
    def get_terrain_color(position:np.ndarray)->np.ndarray:
        '''Get the terrain RGB color at a position in latitude, longitude, and 0.\n
        The Z value of the position is ignored.'''
        position = tuple(position)
        rec = connect.send_message(f"true<<349<<{position}")
        return list(rec[0])

class atmosphere:
    def air_desity()->float:
        '''Get the air density at the current vessel's location in kg/m^3.'''
        rec = connect.send_message(f"true<<130")
        return rec[0]
    def air_pressure()->float:
        '''Get the air pressure at the current vessel's location in Pa.'''
        rec = connect.send_message(f"true<<131")
        return rec[0]
    def speed_of_sound()->float:
        '''Get the speed of sound at the current vessel's location in m/s.'''
        rec = connect.send_message(f"true<<132")
        return rec[0]
    def temperature()->float:
        '''Get the temperature at the current vessel's location in K.'''
        rec = connect.send_message(f"true<<133")
        return rec[0]
    def atmosphere_air_desity(planet:str)->float:
        '''Get the air density at sea level of a planet in kg/m^3.\n'''
        rec = connect.send_message(f"true<<134{planet}")
        return rec[0]
    def atmosphere_height(planet:str)->float:
        '''Get the height of the atmosphere of a planet in meters.\n'''
        rec = connect.send_message(f"true<<135{planet}")
        return rec[0]
    def atmosphere_fade_out(planet:str)->float:
        '''Get the fade out of the atmosphere of a planet in meters.\n'''
        rec = connect.send_message(f"true<<136<<{planet}")
        return rec[0]

class orbit:
    def get_terrain_height(position:np.ndarray)->float:
        '''Get the terrain height at a position in latitude, longitude, and 0.\n
        The Z value of the position is ignored.'''
        position = tuple(position)
        rec = connect.send_message(f"true<<350<<{position}")
        return rec[0]
    def planet_solar_position(planet:str)->np.ndarray:
        '''Get the position of a planet relative to the sun in ECI coordinates in meters.\n'''
        rec = connect.send_message(f"true<<150<<{planet}")
        vec = extra.tuple2array(rec)
        return vec
    def planet_velocity(planet:str)->np.ndarray:
        '''Get the velocity of a planet in ECI coordinates in m/s.\n'''
        rec = connect.send_message(f"true<<151<<{planet}")
        vec = extra.tuple2array(rec)
        return vec
    def planet_apoapsis_position(planet:str)->np.ndarray:
        '''Get the position of a planet's apoapsis in ECI coordinates in meters.\n'''
        rec = connect.send_message(f"true<<152<<{planet}")
        vec = extra.tuple2array(rec)
        return vec
    def planet_periapsis_position(planet:str)->np.ndarray:
        '''Get the position of a planet's periapsis in ECI coordinates in meters.\n'''
        rec = connect.send_message(f"true<<153<<{planet}")
        vec = extra.tuple2array(rec)
        return vec
    def planet_period(planet:str)->float:
        '''Get the orbital period of a planet in seconds.\n'''
        rec = connect.send_message(f"true<<154<<{planet}")
        return rec[0]
    def planet_apoapsis_time(planet:str)->float:
        '''Get the time of apoapsis of a planet in seconds.\n'''
        rec = connect.send_message(f"true<<155<<{planet}")
        return rec[0]
    def planet_periapsis_time(planet:str)->float:
        '''Get the time of periapsis of a planet in seconds.\n'''
        rec = connect.send_message(f"true<<156<<{planet}")
        return rec[0]
    def planet_inclination(planet:str)->float:
        '''Get the inclination of a planet in radians.\n'''
        rec = connect.send_message(f"true<<157<<{planet}")
        return rec[0]
    def planet_eccentricity(planet:str)->float:
        '''Get the eccentricity of a planet.\n'''
        rec = connect.send_message(f"true<<158<<{planet}")
        return rec[0]
    def planet_mean_anomaly(planet:str)->float:
        '''Get the mean anomaly of a planet.\n'''
        rec = connect.send_message(f"true<<159<<{planet}")
        return rec[0]
    def planet_mean_motion(planet:str)->float:
        '''Get the mean motion of a planet in radians/second.\n'''
        rec = connect.send_message(f"true<<160<<{planet}")
        return rec[0]
    def planet_periapsis_argument(planet:str)->float:
        '''Get the argument of periapsis of a planet in radians.\n'''
        rec = connect.send_message(f"true<<161<<{planet}")
        return rec[0]
    def planet_right_ascension(planet:str)->float:
        '''Get the right ascension of a planet in radians.\n'''
        rec = connect.send_message(f"true<<162<<{planet}")
        return rec[0]
    def planet_true_anomaly(planet:str)->float:
        '''Get the true anomaly of a planet in radians.\n'''
        rec = connect.send_message(f"true<<163<<{planet}")
        return rec[0]
    def planet_SMA(planet:str)->float:
        '''Get the semi-major axis of a planet in meters.\n'''
        rec = connect.send_message(f"true<<164<<{planet}")
        return rec[0]
