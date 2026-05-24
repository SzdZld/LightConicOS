from JMOT import connect, extra
import numpy as np

class convert:
    def position2LL_AGL(position:np.ndarray)->np.ndarray:
        '''Convert a position in ECI coordinates to latitude, longitude, and AGL.\n'''
        vec = extra.array2tuple(position)
        rec = connect.send_message(f"true<<345<<{vec}")
        return list(rec[0])
    def position2LL_ASL(position:np.ndarray)->np.ndarray:
        '''Convert a position in ECI coordinates to latitude, longitude, and ASL.\n'''
        vec = extra.array2tuple(position)
        rec = connect.send_message(f"true<<346<<{vec}")
        return list(rec[0])
    def LL_AGL2position(position:np.ndarray)->np.ndarray:
        '''Convert a position in latitude, longitude, and AGL to ECI coordinates.\n'''
        rec = connect.send_message(f"true<<347<<{tuple(position)}")
        vec = extra.tuple2array(rec[0])
        return vec
    def LL_ASL2position(position:np.ndarray)->np.ndarray:
        '''Convert a position in latitude, longitude, and ASL to ECI coordinates.\n'''
        rec = connect.send_message(f"true<<348<<{tuple(position)}")
        vec = extra.tuple2array(rec[0])
        return vec
    def cast_ray(vec1:np.ndarray, vec2:np.ndarray)->np.ndarray:
        '''Cast a ray from vec1 to vec2, and return the position of the first collision in ECI coordinates.\n
        if length out of 100km, return 0.\n'''
        vec1 = extra.array2tuple(vec1)
        vec2 = extra.array2tuple(vec2)
        rec = connect.send_message(f"true<<343<<{vec1}<<{vec2}")
        vec = extra.tuple2array(rec)
        return vec
    def part_loacl_to_eci(partID:int, vector:np.ndarray)->np.ndarray:
        '''Convert part vector in local coordinates of a part to ECI coordinates.\n'''
        v = extra.array2tuple(vector)
        rec = connect.send_message(f"true<<413<<{partID}<<{v}")
        vec = extra.tuple2array(rec[0])
        return vec
    def part_eci_to_local(partID:int, vector:np.ndarray)->np.ndarray:
        '''Convert part vector in ECI coordinates to local coordinates of a part.\n'''
        v = extra.array2tuple(vector)
        rec = connect.send_message(f"true<<414<<{partID}<<{v}")
        vec = extra.tuple2array(rec[0])
        return vec
    
class camera:
    def camera_position()->np.ndarray:
        '''Get the current camera position in ECI coordinates.'''
        rec = connect.send_message(f"true<<352")
        vec = extra.tuple2array(rec)
        return vec
    def camera_pointing()->np.ndarray:
        '''Get the current camera pointing direction in ECI coordinates.'''
        rec = connect.send_message(f"true<<353")
        vec = extra.tuple2array(rec)
        return vec
    def camera_direction()->np.ndarray:
        '''Get the current camera direction in ECI coordinates.'''
        rec = connect.send_message(f"true<<354")
        vec = extra.tuple2array(rec)
        return vec
    
class funk:
    def get_float(funkexpression:str)->float:
        '''Get the value of a funk expression as a float.\n'''
        rec = connect.send_message(f"true<<344<<{funkexpression}")
        return rec[0]
    def get_bool(funkexpression:str)->bool:
        '''Get the value of a funk expression as a boolean.\n'''
        rec = connect.send_message(f"true<<344<<{funkexpression}")
        return bool(rec[0])
    def get_string(funkexpression:str)->str:
        '''Get the value of a funk expression as a string.\n'''
        rec = connect.send_message(f"true<<344<<{funkexpression}")
        return rec[0]
    def get_int(funkexpression:str)->int:
        '''Get the value of a funk expression as an integer.\n'''
        rec = connect.send_message(f"true<<344<<{funkexpression}")
        return rec[0]
    def get_vector(funkexpression:str)->np.ndarray:
        '''Get the value of a funk expression as a vector in ECI coordinates.\n'''
        rec = connect.send_message(f"true<<344<<{funkexpression}")
        return extra.tuple2array(rec[0])