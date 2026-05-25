from JMOT import connect, extra
import numpy as np

_MISC_CONVERT_SIGNALS = {
    "position2LL_AGL":345,
    "position2LL_ASL":346,
    "LL_AGL2position":347,
    "LL_ASL2position":348,
    "cast_ray":343,
    "part_loacl_to_eci":413,
    "part_eci_to_local":414
}

class convert:
    def position2LL_AGL(position:np.ndarray)->np.ndarray:
        '''Convert a position in ECI coordinates to latitude, longitude, and AGL.\n'''
        vec = extra.array2tuple(position)
        rec = connect._send_message(f"true<<{_MISC_CONVERT_SIGNALS['position2LL_AGL']}<<{vec}")
        return list(rec[0])
    def position2LL_ASL(position:np.ndarray)->np.ndarray:
        '''Convert a position in ECI coordinates to latitude, longitude, and ASL.\n'''
        vec = extra.array2tuple(position)
        rec = connect._send_message(f"true<<{_MISC_CONVERT_SIGNALS['position2LL_ASL']}<<{vec}")
        return list(rec[0])
    def LL_AGL2position(position:np.ndarray)->np.ndarray:
        '''Convert a position in latitude, longitude, and AGL to ECI coordinates.\n'''
        rec = connect._send_message(f"true<<{_MISC_CONVERT_SIGNALS['LL_AGL2position']}<<{tuple(position)}")
        vec = extra.tuple2array(rec[0])
        return vec
    def LL_ASL2position(position:np.ndarray)->np.ndarray:
        '''Convert a position in latitude, longitude, and ASL to ECI coordinates.\n'''
        rec = connect._send_message(f"true<<{_MISC_CONVERT_SIGNALS['LL_ASL2position']}<<{tuple(position)}")
        vec = extra.tuple2array(rec[0])
        return vec
    def cast_ray(vec1:np.ndarray, vec2:np.ndarray)->np.ndarray:
        '''Cast a ray from vec1 to vec2, and return the position of the first collision in ECI coordinates.\n
        if length out of 100km, return 0.\n'''
        vec1 = extra.array2tuple(vec1)
        vec2 = extra.array2tuple(vec2)
        rec = connect._send_message(f"true<<{_MISC_CONVERT_SIGNALS['cast_ray']}<<{vec1}<<{vec2}")
        vec = extra.tuple2array(rec)
        return vec
    def part_loacl_to_eci(partID:int, vector:np.ndarray)->np.ndarray:
        '''Convert part vector in local coordinates of a part to ECI coordinates.\n'''
        v = extra.array2tuple(vector)
        rec = connect._send_message(f"true<<{_MISC_CONVERT_SIGNALS['part_loacl_to_eci']}<<{partID}<<{v}")
        vec = extra.tuple2array(rec[0])
        return vec
    def part_eci_to_local(partID:int, vector:np.ndarray)->np.ndarray:
        '''Convert part vector in ECI coordinates to local coordinates of a part.\n'''
        v = extra.array2tuple(vector)
        rec = connect._send_message(f"true<<{_MISC_CONVERT_SIGNALS['part_eci_to_local']}<<{partID}<<{v}")
        vec = extra.tuple2array(rec[0])
        return vec

_MISC_CAMERA_SIGNALS = {
    "camera_position":352,
    "camera_pointing":353,
    "camera_direction":354
}

class camera:
    def camera_position()->np.ndarray:
        '''Get the current camera position in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_MISC_CAMERA_SIGNALS['camera_position']}")
        vec = extra.tuple2array(rec)
        return vec
    def camera_pointing()->np.ndarray:
        '''Get the current camera pointing direction in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_MISC_CAMERA_SIGNALS['camera_pointing']}")
        vec = extra.tuple2array(rec)
        return vec
    def camera_direction()->np.ndarray:
        '''Get the current camera direction in ECI coordinates.'''
        rec = connect._send_message(f"true<<{_MISC_CAMERA_SIGNALS['camera_direction']}")
        vec = extra.tuple2array(rec)
        return vec

_MISC_FUNK_SIGNALS = {
    "get_float":344,
    "get_bool":344,
    "get_string":344,
    "get_int":344
}

class funk:
    def get_float(funkexpression:str)->float:
        '''Get the value of a funk expression as a float.\n'''
        rec = connect._send_message(f"true<<{_MISC_FUNK_SIGNALS['get_float']}<<{funkexpression}")
        return rec[0]
    def get_bool(funkexpression:str)->bool:
        '''Get the value of a funk expression as a boolean.\n'''
        rec = connect._send_message(f"true<<{_MISC_FUNK_SIGNALS['get_bool']}<<{funkexpression}")
        return bool(rec[0])
    def get_string(funkexpression:str)->str:
        '''Get the value of a funk expression as a string.\n'''
        rec = connect._send_message(f"true<<{_MISC_FUNK_SIGNALS['get_string']}<<{funkexpression}")
        return rec[0]
    def get_int(funkexpression:str)->int:
        '''Get the value of a funk expression as an integer.\n'''
        rec = connect._send_message(f"true<<{_MISC_FUNK_SIGNALS['get_int']}<<{funkexpression}")
        return rec[0]
    def get_vector(funkexpression:str)->np.ndarray:
        '''Get the value of a funk expression as a vector in ECI coordinates.\n'''
        rec = connect._send_message(f"true<<{_MISC_FUNK_SIGNALS['get_vector']}<<{funkexpression}")
        return extra.tuple2array(rec[0])