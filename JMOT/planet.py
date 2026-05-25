from JMOT import connect, extra
from typing import Literal
import numpy as np

_PLANET_INFO_SIGNALS = {
    "planet_mass":100,
    "planet_radius":101,
    "is_solid_ground":102,
    "planet_SOI_radius":103,
    "planet_len_of_day":104,
    "planet_len_of_year":105,
    "planet_name_local":106,
    "target_planet":107,
    "planet_parent":108,
    "planet_child_list":109,
    "planet_craft_list":110,
    "planet_craft_ID_list":111,
    "planet_structure_list":112,
    "get_terrain_color":349
}

class info:
    def planet_mass(planet:str)->float:
        '''Get the mass of a planet in kg.\n'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_mass']}<<{planet}")
        return rec[0]
    def planet_radius(planet:str)->float:
        '''Get the radius of a planet in meters.\n'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_radius']}<<{planet}")
        return rec[0]
    def is_solid_ground(planet:str)->bool:
        '''Get the status of whether the surface of a planet is solid.\n
        if solid, return True, else return False.'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['is_solid_ground']}<<{planet}")
        return rec[0]
    def planet_SOI_radius(planet:str)->float:
        '''Get the radius of the sphere of influence of a planet in meters.\n'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_SOI_radius']}<<{planet}")
        return rec[0]
    def planet_len_of_day(planet:str)->float:
        '''Get the length of a day on a planet in seconds.\n'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_len_of_day']}<<{planet}")
        return rec[0]
    def planet_len_of_year(planet:str)->float:
        '''Get the length of a year on a planet in seconds.\n'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_len_of_year']}<<{planet}")
        return rec[0]
    def planet_name_local()->str:
        '''Get the name of the current vessel's main celestial body.'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_name_local']}")
        return rec[0]
    def target_planet()->str:
        '''Get the name of the current vessel's target celestial body.'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['target_planet']}")
        return rec[0]
    def planet_parent(planet:str)->str:
        '''Get the name of the parent body of a planet.\n'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_parent']}<<{planet}")
        return rec[0]
    def planet_child_list(planet:str)->list:
        '''Get the list of child bodies of a planet.'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_child_list']}<<{planet}")
        return rec
    def planet_craft_list(planet:str)->list:
        '''Get the list of craft name in orbit around a planet.'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_craft_list']}<<{planet}")
        return rec
    def planet_craft_ID_list(planet:str)->list:
        '''Get the list of craft ID in orbit around a planet.'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_craft_ID_list']}<<{planet}")
        return rec
    def planet_structure_list(planet:str)->list:
        '''Get the list of structures on a planet.'''
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['planet_structure_list']}<<{planet}")
        return rec
    def get_terrain_color(position:np.ndarray)->np.ndarray:
        '''Get the terrain RGB color at a position in latitude, longitude, and 0.\n
        The Z value of the position is ignored.'''
        position = tuple(position)
        rec = connect._send_message(f"true<<{_PLANET_INFO_SIGNALS['get_terrain_color']}<<{position}")
        return list(rec[0])

_PLANET_ATMOSPHERE_SIGNALS = {
    "air_desity":130,
    "air_pressure":131,
    "speed_of_sound":132,
    "temperature":133,
    "atmosphere_air_desity":134,
    "atmosphere_height":135,
    "atmosphere_fade_out":136
}

class atmosphere:
    def air_desity()->float:
        '''Get the air density at the current vessel's location in kg/m^3.'''
        rec = connect._send_message(f"true<<{_PLANET_ATMOSPHERE_SIGNALS['air_desity']}")
        return rec[0]
    def air_pressure()->float:
        '''Get the air pressure at the current vessel's location in Pa.'''
        rec = connect._send_message(f"true<<{_PLANET_ATMOSPHERE_SIGNALS['air_pressure']}")
        return rec[0]
    def speed_of_sound()->float:
        '''Get the speed of sound at the current vessel's location in m/s.'''
        rec = connect._send_message(f"true<<{_PLANET_ATMOSPHERE_SIGNALS['speed_of_sound']}")
        return rec[0]
    def temperature()->float:
        '''Get the temperature at the current vessel's location in K.'''
        rec = connect._send_message(f"true<<{_PLANET_ATMOSPHERE_SIGNALS['temperature']}")
        return rec[0]
    def atmosphere_air_desity(planet:str)->float:
        '''Get the air density at sea level of a planet in kg/m^3.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ATMOSPHERE_SIGNALS['atmosphere_air_desity']}<<{planet}")
        return rec[0]
    def atmosphere_height(planet:str)->float:
        '''Get the height of the atmosphere of a planet in meters.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ATMOSPHERE_SIGNALS['atmosphere_height']}<<{planet}")
        return rec[0]
    def atmosphere_fade_out(planet:str)->float:
        '''Get the fade out of the atmosphere of a planet in meters.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ATMOSPHERE_SIGNALS['atmosphere_fade_out']}<<{planet}")
        return rec[0]

_PLANET_ORBIT_SIGNALS = {
    "get_terrain_height":350,
    "planet_solar_position":150,
    "planet_velocity":151,
    "planet_apoapsis_position":152,
    "planet_periapsis_position":153,
    "planet_period":154,
    "planet_apoapsis_time":155,
    "planet_periapsis_time":156,
    "planet_inclination":157,
    "planet_eccentricity":158,
    "planet_mean_anomaly":159,
    "planet_mean_motion":160,
    "planet_periapsis_argument":161,
    "planet_right_ascension":162,
    "planet_true_anomaly":163,
    "planet_SMA":164
}

class orbit:
    def get_terrain_height(position:np.ndarray)->float:
        '''Get the terrain height at a position in latitude, longitude, and 0.\n
        The Z value of the position is ignored.'''
        position = tuple(position)
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['get_terrain_height']}<<{position}")
        return rec[0]
    def planet_solar_position(planet:str)->np.ndarray:
        '''Get the position of a planet relative to the sun in ECI coordinates in meters.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_solar_position']}<<{planet}")
        vec = extra.tuple2array(rec)
        return vec
    def planet_velocity(planet:str)->np.ndarray:
        '''Get the velocity of a planet in ECI coordinates in m/s.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_velocity']}<<{planet}")
        vec = extra.tuple2array(rec)
        return vec
    def planet_apoapsis_position(planet:str)->np.ndarray:
        '''Get the position of a planet's apoapsis in ECI coordinates in meters.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_apoapsis_position']}<<{planet}")
        vec = extra.tuple2array(rec)
        return vec
    def planet_periapsis_position(planet:str)->np.ndarray:
        '''Get the position of a planet's periapsis in ECI coordinates in meters.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_periapsis_position']}<<{planet}")
        vec = extra.tuple2array(rec)
        return vec
    def planet_period(planet:str)->float:
        '''Get the orbital period of a planet in seconds.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_period']}<<{planet}")
        return rec[0]
    def planet_apoapsis_time(planet:str)->float:
        '''Get the time of apoapsis of a planet in seconds.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_apoapsis_time']}<<{planet}")
        return rec[0]
    def planet_periapsis_time(planet:str)->float:
        '''Get the time of periapsis of a planet in seconds.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_periapsis_time']}<<{planet}")
        return rec[0]
    def planet_inclination(planet:str)->float:
        '''Get the inclination of a planet in radians.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_inclination']}<<{planet}")
        return rec[0]
    def planet_eccentricity(planet:str)->float:
        '''Get the eccentricity of a planet.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_eccentricity']}<<{planet}")
        return rec[0]
    def planet_mean_anomaly(planet:str)->float:
        '''Get the mean anomaly of a planet.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_mean_anomaly']}<<{planet}")
        return rec[0]
    def planet_mean_motion(planet:str)->float:
        '''Get the mean motion of a planet in radians/second.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_mean_motion']}<<{planet}")
        return rec[0]
    def planet_periapsis_argument(planet:str)->float:
        '''Get the argument of periapsis of a planet in radians.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_periapsis_argument']}<<{planet}")
        return rec[0]
    def planet_right_ascension(planet:str)->float:
        '''Get the right ascension of a planet in radians.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_right_ascension']}<<{planet}")
        return rec[0]
    def planet_true_anomaly(planet:str)->float:
        '''Get the true anomaly of a planet in radians.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_true_anomaly']}<<{planet}")
        return rec[0]
    def planet_SMA(planet:str)->float:
        '''Get the semi-major axis of a planet in meters.\n'''
        rec = connect._send_message(f"true<<{_PLANET_ORBIT_SIGNALS['planet_SMA']}<<{planet}")
        return rec[0]
