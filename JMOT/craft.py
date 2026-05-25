from JMOT import connect, extra
from typing import Literal
import numpy as np

_CRAFT_INFO_SIGNAL = {
    'name' : 200,
    'craftname_of_target' : 201,
    'craftname_of_craftID' : 202,
    'part_count_of_craftID' : 203,
    'craftID_of_craftname' : 204,
    'planet_of_craft' : 205
}

class info:
    def name()->str:
        '''Get the current vessel's name.'''
        rec = connect._send_message(f"true<<{_CRAFT_INFO_SIGNAL['name']}")
        return rec[0]
    def craftname_of_target()->str:
        '''Get the name of the current vessel's target.'''
        rec = connect._send_message(f"true<<{_CRAFT_INFO_SIGNAL['craftname_of_target']}")
        return rec[0]
    def craftname_of_craftID(craft_ID:int)->str:
        '''Get the name of a vessel by its craft ID.'''
        rec = connect._send_message(f"true<<{_CRAFT_INFO_SIGNAL['craftname_of_craftID']}<<{craft_ID}")
        return rec[0]
    def part_count_of_craftID(craft_ID:int)->int:
        '''Get the part count of a vessel by its craft ID.'''
        rec = connect._send_message(f"true<<{_CRAFT_INFO_SIGNAL['part_count_of_craftID']}<<{craft_ID}")
        return rec[0]
    def craftID_of_craftname(craft_name:str)->int:
        '''Get the craft ID of a vessel by its name.'''
        rec = connect._send_message(f"true<<{_CRAFT_INFO_SIGNAL['craftID_of_craftname']}<<{craft_name}")
        return rec[0]
    def planet_of_craft(craft_ID:int)->str:
        '''Get the name of the planet that a vessel is currently orbiting.'''
        rec = connect._send_message(f"true<<{_CRAFT_INFO_SIGNAL['planet_of_craft']}<<{craft_ID}")
        return rec[0]

_CRAFT_FUEL_SIGNAL = {
    'battery' : 225,
    'stage_fuel' : 226,
    'mono_fuel' : 227,
    'all_stage_fuel' : 228
}

class fuel:
    def battery()->float:
        '''Get the current total battery percentage of the vessel.'''
        rec = connect._send_message(f"true<<{_CRAFT_FUEL_SIGNAL['battery']}")
        return rec[0]
    def stage_fuel()->float:
        '''Get the current fuel mass percentage of the active stage.'''
        rec = connect._send_message(f"true<<{_CRAFT_FUEL_SIGNAL['stage_fuel']}")
        return rec[0]
    def mono_fuel()->float:
        '''Get the current monopropellant mass percentage of the vessel.'''
        rec = connect._send_message(f"true<<{_CRAFT_FUEL_SIGNAL['mono_fuel']}")
        return rec[0]
    def all_stage_fuel()->float:
        '''Get the current fuel mass percentage of all stages.'''
        rec = connect._send_message(f"true<<{_CRAFT_FUEL_SIGNAL['all_stage_fuel']}")
        return rec[0]

_CRAFT_PERFORMANCE_SIGNAL = {
    'current_engine_thrust' : 229,
    'mass' : 230,
    'dry_mass' : 231,
    'fuel_mass' : 232,
    'max_engine_thrust' : 233,
    'TWR' : 234,
    'ISP' : 235,
    'stage_delta_v' : 236,
    'stage_burn_time' : 237,
    'solar_radition' : 351,
    'craft_mass' : 238
}

class performance:
    def current_engine_thrust()->float:
        '''Get the current total thrust of all active engines in N.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['current_engine_thrust']}")
        return rec[0]
    def mass()->float:
        '''Get the current mass of the vessel in kg.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['mass']}")
        return rec[0]
    def dry_mass()->float:
        '''Get the current dry mass of the vessel in kg.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['dry_mass']}")
        return rec[0]
    def fuel_mass()->float:
        '''Get the current fuel mass of the vessel in kg.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['fuel_mass']}")
        return rec[0]
    def max_engine_thrust()->float:
        '''Get the maximum total thrust of all engines in N.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['max_engine_thrust']}")
        return rec[0]
    def TWR()->float:
        '''Get the current TWR of the vessel.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['TWR']}")
        return rec[0]
    def ISP()->float:
        '''Get the current ISP of the vessel in seconds.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['ISP']}")
        return rec[0]
    def stage_delta_v()->float:
        '''Get the delta-v of the current stage in m/s.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['stage_delta_v']}")
        return rec[0]
    def stage_burn_time()->float:
        '''Get the burn time of the current stage in seconds.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['stage_burn_time']}")
        return rec[0]
    def solar_radition()->float:
        '''Get the solar radiation at the current vessel's location in W/m^2.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['solar_radition']}")
        return rec[0]
    def craft_mass(craft_ID:int)->float:
        '''Get the mass of a vessel by its craft ID in kg.'''
        rec = connect._send_message(f"true<<{_CRAFT_PERFORMANCE_SIGNAL['craft_mass']}<<{craft_ID}")
        return rec[0]

_CRAFT_POSITION_SIGNAL = {
    'AGL' : 290,
    'ASL' : 291,
    'ASF' : 292,
    'craft_ASL' : 300,
    'is_ground' : 208,
    'craft_is_ground' : 209,
    'ECI_position' : 250,
    'target_ECI_position' : 251,
    'craft_ECI_position' : 252
}

class position:
    def AGL()->float:
        '''Get the current vessel's altitude above ground level in meters.'''
        rec = connect._send_message(f"true<<{_CRAFT_POSITION_SIGNAL['AGL']}")
        return rec[0]
    def ASL()->float:
        '''Get the current vessel's altitude above sea level in meters.'''
        rec = connect._send_message(f"true<<{_CRAFT_POSITION_SIGNAL['ASL']}")
        return rec[0]
    def ASF()->float:
        '''Get the current vessel's altitude above seabed in meters.'''
        rec = connect._send_message(f"true<<{_CRAFT_POSITION_SIGNAL['ASF']}")
        return rec[0]
    def craft_ASL(craft_ID:int)->float:
        '''Get the altitude above sea level of a vessel in meters.'''
        rec = connect._send_message(f"true<<{_CRAFT_POSITION_SIGNAL['craft_ASL']}<<{craft_ID}")
        return rec[0]
    def is_ground()->bool:
        '''Get whether the current vessel is on the ground.\n
        T means the vessel is on the ground, F means it's not.
        '''
        rec = connect._send_message(f"true<<{_CRAFT_POSITION_SIGNAL['is_ground']}")
        return rec[0]
    def craft_is_ground(craft_id:int)->bool:
        '''Get whether a vessel is on the ground.\n
        T means the vessel is on the ground, F means it's not.
        '''
        rec = connect._send_message(f"true<<{_CRAFT_POSITION_SIGNAL['craft_is_ground']}<<{craft_id}")
        return rec[0]
    def ECI_position()->np.ndarray:
        '''Get the current vessel's position in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_POSITION_SIGNAL['ECI_position']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def target_ECI_position()->np.ndarray:
        '''Get the target vessel's position in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_POSITION_SIGNAL['target_ECI_position']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_ECI_position(craft_ID:int)->np.ndarray:
        '''Get the position of a vessel by its craft ID in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_POSITION_SIGNAL['craft_ECI_position']}<<{craft_ID}")
        vec = extra.tuple2array(rec[0])
        return vec

_CRAFT_ATTITUDE_SIGNAL = {
    'craft_heading' : 255,
    'craft_pitching' : 256,
    'craft_autopilot_heading' : 257,
    'craft_autopilot_pitching' : 258,
    'craft_bank_angle' : 259,
    'craft_AOA' : 260,
    'craft_side_slip': 261,
    'craft_north_vector' : 262,
    'craft_east_vector' : 263,
    'craft_roll_axis' : 264,
    'craft_pitch_axis' : 265,
    'craft_yaw_axis' : 266
}

class attitude:
    def craft_heading()->float:
        '''
        Get the current vessel's heading in degrees.\n
        0 degrees means the vessel is heading towards the north
        and the angle increases clockwise.
        '''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_heading']}")
        return rec[0]
    def craft_pitching()->float:
        '''
        Get the current vessel's pitching in degrees.\n
        90 degrees means the vessel is flying vertically,
        0 degrees means the vessel is flying horizontally.
        '''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_pitching']}")
        return rec[0]
    def craft_autopilot_heading()->float:
        '''Get the current vessel's autopilot heading in degrees.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_autopilot_heading']}")
        return rec[0]
    def craft_autopilot_pitching()->float:
        '''Get the current vessel's autopilot pitching in degrees.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_autopilot_pitching']}")
        return rec[0]
    def craft_bank_angle()->float:
        '''Get the current vessel's bank angle in degrees.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_bank_angle']}")
        return rec[0]
    def craft_AOA()->float:
        '''Get the current vessel's angle of attack in degrees.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_AOA']}")
        return rec[0]
    def craft_side_slip()->float:
        '''Get the current vessel's side slip angle in degrees.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_side_slip']}")
        return rec[0]
    def craft_north_vector()->np.ndarray:
        '''Get the current vessel's north vector in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_north_vector']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_east_vector()->np.ndarray:
        '''Get the current vessel's east vector in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_east_vector']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_roll_axis()->np.ndarray:
        '''Get the current vessel's roll axis in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_roll_axis']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_pitch_axis()->np.ndarray:
        '''Get the current vessel's pitch axis in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_pitch_axis']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_yaw_axis()->np.ndarray:
        '''Get the current vessel's yaw axis in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_ATTITUDE_SIGNAL['craft_yaw_axis']}")
        vec = extra.tuple2array(rec[0])
        return vec

_CRAFT_VELOCITY_SIGNAL = {
    'surface_velocity' : 270,
    'orbit_velocity' : 271,
    'target_velocity' : 272,
    'gravity' : 273,
    'drag' : 274,
    'acceleration' : 275,
    'angular' : 276,
    'lateral' : 277,
    'vertical' : 278,
    'mach_number' : 279,
    'craft_velocity' : 280
}

class velocity:
    def surface_velocity()->np.ndarray:
        '''Get the current vessel's surface velocity in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['surface_velocity']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def orbit_velocity()->np.ndarray:
        '''Get the current vessel's orbit velocity in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['orbit_velocity']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def target_velocity()->np.ndarray:
        '''Get the current vessel's target velocity in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['target_velocity']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def gravity()->np.ndarray:
        '''Get the current vessel's gravity in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['gravity']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def drag()->np.ndarray:
        '''Get the current vessel's drag in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['drag']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def acceleration()->np.ndarray:
        '''Get the current vessel's acceleration in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['acceleration']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def angular()->np.ndarray:
        '''Get the current vessel's angular velocity in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['angular']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def lateral()->float:
        '''Get the current vessel's lateral velocity in m/s.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['lateral']}")
        return rec[0]
    def vertical()->float:
        '''Get the current vessel's vertical velocity in m/s.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['vertical']}")
        return rec[0]
    def mach_number()->float:
        '''Get the current vessel's Mach number.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['mach_number']}")
        return rec[0]
    def craft_velocity(craft_ID:int)->np.ndarray:
        '''Get the velocity of a vessel by its craft ID in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_VELOCITY_SIGNAL['craft_velocity']}")
        vec = extra.tuple2array(rec[0])
        return vec

_CRAFT_ORBIT_SIGNAL = {
    'apoapsis' : 293,
    'periapsis' : 294,
    'apoapsis_time' : 295,
    'periapsis_time' : 296,
    'eccentricity' : 297,
    'inclination' : 298,
    'period' : 299,
    'craft_apoapsis_position' : 301,
    'craft_periapsis_position' : 302,
    'craft_period' : 303,
    'craft_apoapsis_time' : 304,
    'craft_periapsis_time' : 305,
    'craft_inclination' : 306,
    'craft_eccentricity' : 307,
    'craft_mean_anomaly' : 308,
    'craft_mean_motion' : 309,
    'craft_periapsis_argument' : 310,
    'craft_right_ascension' : 311,
    'craft_true_anomaly' : 312,
    'craft_SMA' : 313
}

class orbit:
    def apoapsis()->float:
        '''Get the current vessel's apoapsis altitude in meters.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['apoapsis']}")
        return rec[0]
    def periapsis()->float:
        '''Get the current vessel's periapsis altitude in meters.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['periapsis']}")
        return rec[0]
    def apoapsis_time()->float:
        '''Get the time to current vessel's apoapsis in seconds.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['apoapsis_time']}")
        return rec[0]
    def periapsis_time()->float:
        '''Get the time to current vessel's periapsis in seconds.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['periapsis_time']}")
        return rec[0]
    def eccentricity()->float:
        '''Get the eccentricity of the current vessel's orbit.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['eccentricity']}")
        return rec[0]
    def inclination()->float:
        '''Get the inclination of the current vessel's orbit in radians.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['inclination']}")
        return rec[0]
    def period()->float:
        '''Get the current vessel's orbital period in seconds.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['period']}")
        return rec[0]
    def craft_apoapsis_position(craft_ID:int)->np.ndarray:
        '''Get the apoapsis position of a vessel by its craft ID in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_apoapsis_position']}<<{craft_ID}")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_periapsis_position(craft_ID:int)->np.ndarray:
        '''Get the periapsis position of a vessel by its craft ID in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_periapsis_position']}<<{craft_ID}")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_period(craft_ID:int)->float:
        '''Get the orbital period of a vessel by its craft ID in seconds.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_period']}<<{craft_ID}")
        return rec[0]
    def craft_apoapsis_time(craft_ID:int)->float:
        '''Get the time to current vessel'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_apoapsis_time']}<<{craft_ID}")
        return rec[0]
    def craft_periapsis_time(craft_ID:int)->float:
        '''Get the time to current vessel's periapsis in seconds.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_periapsis_time']}<<{craft_ID}")
        return rec[0]
    def craft_inclination(craft_ID:int)->float:
        '''Get the inclination of a vessel by its craft ID in radians.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_inclination']}<<{craft_ID}")
        return rec[0]
    def craft_eccentricity(craft_ID:int)->float:
        '''Get the eccentricity of a vessel by its craft ID.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_eccentricity']}<<{craft_ID}")
        return rec[0]
    def craft_mean_anomaly(craft_ID:int)->float:
        '''Get the mean anomaly of a vessel by its craft ID in radians.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_mean_anomaly']}<<{craft_ID}")
        return rec[0]
    def craft_mean_motion(craft_ID:int)->float:
        '''Get the mean motion of a vessel by its craft ID in radians/second.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_mean_motion']}<<{craft_ID}")
        return rec[0]
    def craft_periapsis_argument(craft_ID:int)->float:
        '''Get the argument of periapsis of a vessel by its craft ID in radians.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_periapsis_argument']}<<{craft_ID}")
        return rec[0]
    def craft_right_ascension(craft_ID:int)->float:
        '''Get the right ascension of a vessel by its craft ID in radians.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_right_ascension']}<<{craft_ID}")
        return rec[0]
    def craft_true_anomaly(craft_ID:int)->float:
        '''Get the true anomaly of a vessel by its craft ID in radians.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_true_anomaly']}<<{craft_ID}")
        return rec[0]
    def craft_SMA(craft_ID:int)->float:
        '''Get the semi-major axis of a vessel by its craft ID in meters.'''
        rec = connect._send_message(f"true<<{_CRAFT_ORBIT_SIGNAL['craft_SMA']}<<{craft_ID}")
        return rec[0]

_CRAFT_INPUT_SIGNAL = {
    'roll' : 320,
    'pitch' : 321,
    'yaw' : 322,
    'throttle' : 323,
    'brake' : 324,
    'slider1' : 325,
    'slider2' : 326,
    'slider3' : 327,
    'slider4' : 328,
    'translate_foraward' : 329,
    'translate_right' : 330,
    'translate_up' : 331,
    'translate_mode' : 332,
    'pitch_pids' : 333,
    'roll_pids' : 334
}

class input:
    def roll()->float:
        '''Get the current vessel's roll input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['roll']}")
        return rec[0]
    def pitch()->float:
        '''Get the current vessel's pitch input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['pitch']}")
        return rec[0]
    def yaw()->float:
        '''Get the current vessel's yaw input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['yaw']}")
        return rec[0]
    def throttle()->float:
        '''Get the current vessel's throttle input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['throttle']}")
        return rec[0]
    def brake()->float:
        '''Get the current vessel's brake input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['brake']}")
        return rec[0]
    def slider1()->float:
        '''Get the current vessel's slider1 input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['slider1']}")
        return rec[0]
    def slider2()->float:
        '''Get the current vessel's slider2 input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['slider2']}")
        return rec[0]
    def slider3()->float:
        '''Get the current vessel's slider3 input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['slider3']}")
        return rec[0]
    def slider4()->float:
        '''Get the current vessel's slider4 input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['slider4']}")
        return rec[0]
    def translate_foraward()->float:
        '''Get the current vessel's forward translation input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['translate_foraward']}")
        return rec[0]
    def translate_right()->float:
        '''Get the current vessel's right translation input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['translate_right']}")
        return rec[0]
    def translate_up()->float:
        '''Get the current vessel's up translation input value.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['translate_up']}")
        return rec[0]
    def translate_mode()->float:
        '''
        Get the current vessel's translation mode input value.\n
        0.0 is attitude mode, 1.0 is translate_mode.
        '''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['translate_mode']}")
        return rec[0]
    def pitch_pids()->np.ndarray:
        '''Get the current vessel's pitch PID values as a numpy array.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['pitch_pids']}")
        vec = extra.tuple2array(rec[0])
        return vec
    def roll_pids()->np.ndarray:
        '''Get the current vessel's roll PID values as a numpy array.'''
        rec = connect._send_message(f"true<<{_CRAFT_INPUT_SIGNAL['roll_pids']}")
        vec = extra.tuple2array(rec[0])
        return vec
    
_CRAFT_STATUS_SIGNAL = {
    'activing_stage' : 340,
    'num_of_stage' : 341,
    'ag_status' : 342,
    'craft_is_destroyed' : 206,
    'craft_is_player' : 207
}

class status:
    def activing_stage()->int:
        '''Get the current active stage number.'''
        rec = connect._send_message(f"true<<{_CRAFT_STATUS_SIGNAL['activing_stage']}")
        return rec[0]
    def num_of_stage()->int:
        '''Get the total number of stages.'''
        rec = connect._send_message(f"true<<{_CRAFT_STATUS_SIGNAL['num_of_stage']}")
        return rec[0]
    def ag_status(ag:int)->bool:
        '''Get the status of an action group.\n'''
        rec = connect._send_message(f"true<<{_CRAFT_STATUS_SIGNAL['ag_status']}<<{ag}")
        return rec[0]
    def craft_is_destroyed(craft_ID:int)->bool:
        '''Get the status of whether a vessel is destroyed.\n'''
        rec = connect._send_message(f"true<<{_CRAFT_STATUS_SIGNAL['craft_is_destroyed']}<<{craft_ID}")
        return rec[0]
    def craft_is_player(craft_ID:int)->bool:
        '''Get the status of whether a vessel is a player vessel.\n'''
        rec = connect._send_message(f"true<<{_CRAFT_STATUS_SIGNAL['craft_is_player']}<<{craft_ID}")
        return rec[0]