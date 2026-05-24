from JMOT import connect, extra
from typing import Literal
import numpy as np


class info:
    def name()->str:
        '''Get the current vessel's name.'''
        rec = connect.send_message(f"true<<200")
        return rec[0]
    def craftname_of_target()->str:
        '''Get the name of the current vessel's target.'''
        rec = connect.send_message(f"true<<201")
        return rec[0]
    def craftname_of_craftID(craft_ID:int)->str:
        '''Get the name of a vessel by its craft ID.'''
        rec = connect.send_message(f"true<<202<<{craft_ID}")
        return rec[0]
    def part_count_of_craftID(craft_ID:int)->int:
        '''Get the part count of a vessel by its craft ID.'''
        rec = connect.send_message(f"true<<203<<{craft_ID}")
        return rec[0]
    def craftID_of_craftname(craft_name:str)->int:
        '''Get the craft ID of a vessel by its name.'''
        rec = connect.send_message(f"true<<204<<{craft_name}")
        return rec[0]
    def planet_of_craft(craft_ID:int)->str:
        '''Get the name of the planet that a vessel is currently orbiting.'''
        rec = connect.send_message(f"true<<205<<{craft_ID}")
        return rec[0]

class fuel:
    def battery()->float:
        '''Get the current total battery percentage of the vessel.'''
        rec = connect.send_message(f"true<<225")
        return rec[0]
    def stage_fuel()->float:
        '''Get the current fuel mass percentage of the active stage.'''
        rec = connect.send_message(f"true<<226")
        return rec[0]
    def mono_fuel()->float:
        '''Get the current monopropellant mass percentage of the vessel.'''
        rec = connect.send_message(f"true<<227")
        return rec[0]
    def all_stage_fuel()->float:
        '''Get the current fuel mass percentage of all stages.'''
        rec = connect.send_message(f"true<<228")
        return rec[0]

class performance:
    def current_engine_thrust()->float:
        '''Get the current total thrust of all active engines in N.'''
        rec = connect.send_message(f"true<<229")
        return rec[0]
    def mass()->float:
        '''Get the current mass of the vessel in kg.'''
        rec = connect.send_message(f"true<<230")
        return rec[0]
    def dry_mass()->float:
        '''Get the current dry mass of the vessel in kg.'''
        rec = connect.send_message(f"true<<231")
        return rec[0]
    def fuel_mass()->float:
        '''Get the current fuel mass of the vessel in kg.'''
        rec = connect.send_message(f"true<<232")
        return rec[0]
    def max_engine_thrust()->float:
        '''Get the maximum total thrust of all engines in N.'''
        rec = connect.send_message(f"true<<233")
        return rec[0]
    def TWR()->float:
        '''Get the current TWR of the vessel.'''
        rec = connect.send_message(f"true<<234")
        return rec[0]
    def ISP()->float:
        '''Get the current ISP of the vessel in seconds.'''
        rec = connect.send_message(f"true<<235")
        return rec[0]
    def stage_delta_v()->float:
        '''Get the delta-v of the current stage in m/s.'''
        rec = connect.send_message(f"true<<236")
        return rec[0]
    def stage_burn_time()->float:
        '''Get the burn time of the current stage in seconds.'''
        rec = connect.send_message(f"true<<237")
        return rec[0]
    def solar_radition()->float:
        '''Get the solar radiation at the current vessel's location in W/m^2.'''
        rec = connect.send_message(f"true<<351")
        return rec[0]
    def craft_mass(craft_ID:int)->float:
        '''Get the mass of a vessel by its craft ID in kg.'''
        rec = connect.send_message(f"true<<238<<{craft_ID}")
        return rec[0]

class position:
    def AGL()->float:
        '''Get the current vessel's altitude above ground level in meters.'''
        rec = connect.send_message(f"true<<290")
        return rec[0]
    def ASL()->float:
        '''Get the current vessel's altitude above sea level in meters.'''
        rec = connect.send_message(f"true<<291")
        return rec[0]
    def ASF()->float:
        '''Get the current vessel's altitude above seabed in meters.'''
        rec = connect.send_message(f"true<<292")
        return rec[0]
    def craft_ASL(craft_ID:int)->float:
        '''Get the altitude above sea level of a vessel in meters.'''
        rec = connect.send_message(f"true<<300<<{craft_ID}")
        return rec[0]
    def is_ground()->bool:
        '''Get whether the current vessel is on the ground.\n
        T means the vessel is on the ground, F means it's not.
        '''
        rec = connect.send_message(f"true<<208")
        return rec[0]
    def craft_is_ground(craft_id:int)->bool:
        '''Get whether a vessel is on the ground.\n
        T means the vessel is on the ground, F means it's not.
        '''
        rec = connect.send_message(f"true<<209<<{craft_id}")
        return rec[0]
    def ECI_position()->np.ndarray:
        '''Get the current vessel's position in ECI coordinates.'''
        rec = connect.send_message(f"true<<250")
        vec = extra.tuple2array(rec[0])
        return vec
    def target_ECI_position()->np.ndarray:
        '''Get the target vessel's position in ECI coordinates.'''
        rec = connect.send_message(f"true<<251")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_ECI_position(craft_ID:int)->np.ndarray:
        '''Get the position of a vessel by its craft ID in ECI coordinates.'''
        rec = connect.send_message(f"true<<252<<{craft_ID}")
        vec = extra.tuple2array(rec[0])
        return vec

class attitude:
    def craft_heading()->float:
        '''
        Get the current vessel's heading in degrees.\n
        0 degrees means the vessel is heading towards the north
        and the angle increases clockwise.
        '''
        rec = connect.send_message(f"true<<255")
        return rec[0]
    def craft_pitching()->float:
        '''
        Get the current vessel's pitching in degrees.\n
        90 degrees means the vessel is flying vertically,
        0 degrees means the vessel is flying horizontally.
        '''
        rec = connect.send_message(f"true<<256")
        return rec[0]
    def craft_autopilot_heading()->float:
        '''Get the current vessel's autopilot heading in degrees.'''
        rec = connect.send_message(f"true<<257")
        return rec[0]
    def craft_autopilot_pitching()->float:
        '''Get the current vessel's autopilot pitching in degrees.'''
        rec = connect.send_message(f"true<<258")
        return rec[0]
    def craft_bank_angle()->float:
        '''Get the current vessel's bank angle in degrees.'''
        rec = connect.send_message(f"true<<259")
        return rec[0]
    def craft_AOA()->float:
        '''Get the current vessel's angle of attack in degrees.'''
        rec = connect.send_message(f"true<<260")
        return rec[0]
    def craft_side_slip()->float:
        '''Get the current vessel's side slip angle in degrees.'''
        rec = connect.send_message(f"true<<261")
        return rec[0]
    def craft_north_vector()->np.ndarray:
        '''Get the current vessel's north vector in ECI coordinates.'''
        rec = connect.send_message(f"true<<262")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_east_vector()->np.ndarray:
        '''Get the current vessel's east vector in ECI coordinates.'''
        rec = connect.send_message(f"true<<263")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_roll_axis()->np.ndarray:
        '''Get the current vessel's roll axis in ECI coordinates.'''
        rec = connect.send_message(f"true<<264")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_pitch_axis()->np.ndarray:
        '''Get the current vessel's pitch axis in ECI coordinates.'''
        rec = connect.send_message(f"true<<265")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_yaw_axis()->np.ndarray:
        '''Get the current vessel's yaw axis in ECI coordinates.'''
        rec = connect.send_message(f"true<<266")
        vec = extra.tuple2array(rec[0])
        return vec


class velocity:
    def surface_velocity()->np.ndarray:
        '''Get the current vessel's surface velocity in ECI coordinates.'''
        rec = connect.send_message(f"true<<270")
        vec = extra.tuple2array(rec[0])
        return vec
    def orbit_velocity()->np.ndarray:
        '''Get the current vessel's orbit velocity in ECI coordinates.'''
        rec = connect.send_message(f"true<<271")
        vec = extra.tuple2array(rec[0])
        return vec
    def target_velocity()->np.ndarray:
        '''Get the current vessel's target velocity in ECI coordinates.'''
        rec = connect.send_message(f"true<<272")
        vec = extra.tuple2array(rec[0])
        return vec
    def gravity()->np.ndarray:
        '''Get the current vessel's gravity in ECI coordinates.'''
        rec = connect.send_message(f"true<<273")
        vec = extra.tuple2array(rec[0])
        return vec
    def drag()->np.ndarray:
        '''Get the current vessel's drag in ECI coordinates.'''
        rec = connect.send_message(f"true<<274")
        vec = extra.tuple2array(rec[0])
        return vec
    def acceleration()->np.ndarray:
        '''Get the current vessel's acceleration in ECI coordinates.'''
        rec = connect.send_message(f"true<<275")
        vec = extra.tuple2array(rec[0])
        return vec
    def angular()->np.ndarray:
        '''Get the current vessel's angular velocity in ECI coordinates.'''
        rec = connect.send_message(f"true<<276")
        vec = extra.tuple2array(rec[0])
        return vec
    def lateral()->float:
        '''Get the current vessel's lateral velocity in m/s.'''
        rec = connect.send_message(f"true<<277")
        return rec[0]
    def vertical()->float:
        '''Get the current vessel's vertical velocity in m/s.'''
        rec = connect.send_message(f"true<<278")
        return rec[0]
    def mach_number()->float:
        '''Get the current vessel's Mach number.'''
        rec = connect.send_message(f"true<<278")
        return rec[0]
    def craft_velocity(craft_ID:int)->np.ndarray:
        '''Get the velocity of a vessel by its craft ID in ECI coordinates.'''
        rec = connect.send_message(f"true<<280")
        vec = extra.tuple2array(rec[0])
        return vec

class orbit:
    def apoapsis()->float:
        '''Get the current vessel's apoapsis altitude in meters.'''
        rec = connect.send_message(f"true<<293")
        return rec[0]
    def periapsis()->float:
        '''Get the current vessel's periapsis altitude in meters.'''
        rec = connect.send_message(f"true<<294")
        return rec[0]
    def apoapsis_time()->float:
        '''Get the time to current vessel's apoapsis in seconds.'''
        rec = connect.send_message(f"true<<295")
        return rec[0]
    def periapsis_time()->float:
        '''Get the time to current vessel's periapsis in seconds.'''
        rec = connect.send_message(f"true<<296")
        return rec[0]
    def eccentricity()->float:
        '''Get the eccentricity of the current vessel's orbit.'''
        rec = connect.send_message(f"true<<297")
        return rec[0]
    def inclination()->float:
        '''Get the inclination of the current vessel's orbit in radians.'''
        rec = connect.send_message(f"true<<298")
        return rec[0]
    def period()->float:
        '''Get the current vessel's orbital period in seconds.'''
        rec = connect.send_message(f"true<<299")
        return rec[0]
    def craft_apoapsis_position(craft_ID:int)->np.ndarray:
        '''Get the apoapsis position of a vessel by its craft ID in ECI coordinates.'''
        rec = connect.send_message(f"true<<301<<{craft_ID}")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_periapsis_position(craft_ID:int)->np.ndarray:
        '''Get the periapsis position of a vessel by its craft ID in ECI coordinates.'''
        rec = connect.send_message(f"true<<302<<{craft_ID}")
        vec = extra.tuple2array(rec[0])
        return vec
    def craft_period(craft_ID:int)->float:
        '''Get the orbital period of a vessel by its craft ID in seconds.'''
        rec = connect.send_message(f"true<<303<<{craft_ID}")
        return rec[0]
    def craft_apoapsis_time(craft_ID:int)->float:
        '''Get the time to current vessel'''
        rec = connect.send_message(f"true<<304<<{craft_ID}")
        return rec[0]
    def craft_periapsis_time(craft_ID:int)->float:
        '''Get the time to current vessel's periapsis in seconds.'''
        rec = connect.send_message(f"true<<305<<{craft_ID}")
        return rec[0]
    def craft_inclination(craft_ID:int)->float:
        '''Get the inclination of a vessel by its craft ID in radians.'''
        rec = connect.send_message(f"true<<306<<{craft_ID}")
        return rec[0]
    def craft_eccentricity(craft_ID:int)->float:
        '''Get the eccentricity of a vessel by its craft ID.'''
        rec = connect.send_message(f"true<<307<<{craft_ID}")
        return rec[0]
    def craft_mean_anomaly(craft_ID:int)->float:
        '''Get the mean anomaly of a vessel by its craft ID in radians.'''
        rec = connect.send_message(f"true<<308<<{craft_ID}")
        return rec[0]
    def craft_mean_motion(craft_ID:int)->float:
        '''Get the mean motion of a vessel by its craft ID in radians/second.'''
        rec = connect.send_message(f"true<<309<<{craft_ID}")
        return rec[0]
    def craft_periapsis_argument(craft_ID:int)->float:
        '''Get the argument of periapsis of a vessel by its craft ID in radians.'''
        rec = connect.send_message(f"true<<310<<{craft_ID}")
        return rec[0]
    def craft_right_ascension(craft_ID:int)->float:
        '''Get the right ascension of a vessel by its craft ID in radians.'''
        rec = connect.send_message(f"true<<311<<{craft_ID}")
        return rec[0]
    def craft_true_anomaly(craft_ID:int)->float:
        '''Get the true anomaly of a vessel by its craft ID in radians.'''
        rec = connect.send_message(f"true<<312<<{craft_ID}")
        return rec[0]
    def craft_SMA(craft_ID:int)->float:
        '''Get the semi-major axis of a vessel by its craft ID in meters.'''
        rec = connect.send_message(f"true<<313<<{craft_ID}")
        return rec[0]
    
class input:
    def roll()->float:
        '''Get the current vessel's roll input value.'''
        rec = connect.send_message(f"true<<320")
        return rec[0]
    def pitch()->float:
        '''Get the current vessel's pitch input value.'''
        rec = connect.send_message(f"true<<321")
        return rec[0]
    def yaw()->float:
        '''Get the current vessel's yaw input value.'''
        rec = connect.send_message(f"true<<322")
        return rec[0]
    def throttle()->float:
        '''Get the current vessel's throttle input value.'''
        rec = connect.send_message(f"true<<323")
        return rec[0]
    def brake()->float:
        '''Get the current vessel's brake input value.'''
        rec = connect.send_message(f"true<<324")
        return rec[0]
    def slider1()->float:
        '''Get the current vessel's slider1 input value.'''
        rec = connect.send_message(f"true<<325")
        return rec[0]
    def slider2()->float:
        '''Get the current vessel's slider2 input value.'''
        rec = connect.send_message(f"true<<326")
        return rec[0]
    def slider3()->float:
        '''Get the current vessel's slider3 input value.'''
        rec = connect.send_message(f"true<<327")
        return rec[0]
    def slider4()->float:
        '''Get the current vessel's slider4 input value.'''
        rec = connect.send_message(f"true<<328")
        return rec[0]
    def translate_foraward()->float:
        '''Get the current vessel's forward translation input value.'''
        rec = connect.send_message(f"true<<329")
        return rec[0]
    def translate_right()->float:
        '''Get the current vessel's right translation input value.'''
        rec = connect.send_message(f"true<<330")
        return rec[0]
    def translate_up()->float:
        '''Get the current vessel's up translation input value.'''
        rec = connect.send_message(f"true<<331")
        return rec[0]
    def translate_mode()->float:
        '''
        Get the current vessel's translation mode input value.\n
        0.0 is attitude mode, 1.0 is translate_mode.
        '''
        rec = connect.send_message(f"true<<332")
        return rec[0]
    def pitch_pids()->np.ndarray:
        '''Get the current vessel's pitch PID values as a numpy array.'''
        rec = connect.send_message(f"true<<333")
        vec = extra.tuple2array(rec[0])
        return vec
    def roll_pids()->np.ndarray:
        '''Get the current vessel's roll PID values as a numpy array.'''
        rec = connect.send_message(f"true<<334")
        vec = extra.tuple2array(rec[0])
        return vec
    
class status:
    def activing_stage()->int:
        '''Get the current active stage number.'''
        rec = connect.send_message(f"true<<340")
        return rec[0]
    def num_of_stage()->int:
        '''Get the total number of stages.'''
        rec = connect.send_message(f"true<<341")
        return rec[0]
    def ag_status(ag:int)->bool:
        '''Get the status of an action group.\n'''
        rec = connect.send_message(f"true<<342<<{ag}")
        return rec[0]
    def craft_is_destroyed(craft_ID:int)->bool:
        '''Get the status of whether a vessel is destroyed.\n'''
        rec = connect.send_message(f"true<<206<<{craft_ID}")
        return rec[0]
    def craft_is_player(craft_ID:int)->bool:
        '''Get the status of whether a vessel is a player vessel.\n'''
        rec = connect.send_message(f"true<<207<<{craft_ID}")
        return rec[0]