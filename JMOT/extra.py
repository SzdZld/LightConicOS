import math
import numpy as np

def tuple2array(vec:tuple[float, float, float])->np.ndarray:
    '''Convert a tuple to a numpy array, and swap the second and third elements'''
    vec = list(vec)
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    return np.array(vec)

def array2tuple(vec:np.ndarray)->tuple[float, float, float]:
    '''Convert a numpy array to a tuple, and swap the second and third elements'''
    vec = vec.tolist()
    tmp = vec[1]
    vec[1] = vec[2]
    vec[2] = tmp
    vec = tuple(vec)
    return vec

    """
    修复 JMOT 底层暴力拆解导致的列表错位问题。
    将被切碎的 '[1'、'3)]' 等残骸重新拼接回完整的数字和元组。
    """
    if not raw_list:
        return []
        
    result = []
    i = 0
    
    while i < len(raw_list):
        item = str(raw_list[i])
        
        # 1. 处理被切断的列表开头：比如 '[1' 
        if item.startswith('['):
            clean_num = item.lstrip("[").strip("' ")
            try:
                result.append(float(clean_num))
            except ValueError:
                result.append(clean_num)
                
        # 2. 处理被切断的元组：寻找以 '(' 开头但不以 ')' 结尾的碎片
        elif item.startswith('(') and not item.endswith(')'):
            tuple_parts = [item]
            # 一直往后找，直到遇到以 ')' 结尾的碎片
            j = i + 1
            while j < len(raw_list):
                tuple_parts.append(str(raw_list[j]))
                if str(raw_list[j]).endswith(')'):
                    break
                j += 1
            
            # 把碎片拼起来，例如 "(1" + "2.0" + "3)" -> "(12.03)"
            full_tuple_str = "".join(tuple_parts)
            
            # 提取括号内的内容并转为浮点数元组
            inner = full_tuple_str.strip("()")
            try:
                nums = [float(x.strip()) for x in inner.split(",")]
                result.append(tuple(nums))
            except ValueError:
                result.append(full_tuple_str)  # 转换失败则保留原样
                
            i = j  # 跳过已经处理过的碎片
            
        # 3. 处理普通的中间元素（如 "'aaa'" 或 3.14）
        else:
            clean_item = item.strip("' ")
            try:
                result.append(float(clean_item))
            except ValueError:
                result.append(clean_item)
                
        i += 1
        
    return result

def eci2ecef(r_eci, total_seconds):
    '''DO NOT USE THIS FUNCTION, IT IS NOT ACCURATE ENOUGH'''
    theta = 2 * np.pi * (total_seconds / 86400)
    r_eci = np.array([r_eci[0], r_eci[1], r_eci[2]])
    Rz = np.array([
        [np.cos(theta), np.sin(theta), 0],
        [-np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    
    r_ecef = Rz @ r_eci
    return r_ecef

def lla2ecef(lon, lat, h, R=6371010.0):
    '''DO NOT USE THIS FUNCTION, IT IS NOT ACCURATE ENOUGH'''
    lon_rad = np.radians(lon)
    lat_rad = np.radians(lat)
    X = (R + h) * np.cos(lat_rad) * np.cos(lon_rad)
    Y = (R + h) * np.cos(lat_rad) * np.sin(lon_rad)
    Z = (R + h) * np.sin(lat_rad)
    return np.array([X, Y, Z])


def ecef2enu(lon, lat, v_ECEF):
    '''DO NOT USE THIS FUNCTION, IT IS NOT ACCURATE ENOUGH'''
    lon = np.radians(lon)
    lat = np.radians(lat)
    v_ECEF = np.array([v_ECEF[0], v_ECEF[1], v_ECEF[2]])

    R = np.array([
        [-np.sin(lon), np.cos(lon), 0],
        [-np.sin(lat) * np.cos(lon), -np.sin(lat) * np.sin(lon), np.cos(lat)],
        [np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon), np.sin(lat)]
    ])
    
    return R @ v_ECEF


def enu_to_pitch_heading(v_e, v_n, v_u):
    '''DO NOT USE THIS FUNCTION, IT IS NOT ACCURATE ENOUGH'''
    heading = np.degrees(np.arctan2(v_e, v_n))
    
    norm = np.sqrt(v_e**2 + v_n**2 + v_u**2)
    pitch = np.degrees(np.arcsin(v_u / norm))
    
    return pitch, heading


def eci_to_enu_velocity(r_eci, v_eci):
    '''DO NOT USE THIS FUNCTION, IT IS NOT ACCURATE ENOUGH'''
    """Convert ECI velocity to ENU velocity."""
    x, y, z = r_eci
    vx, vy, vz = v_eci
    
    # Compute longitude (lambda) and latitude (phi)
    lambda_ = math.atan2(y, x)  # Longitude
    phi = math.atan2(z, math.sqrt(x**2 + y**2))  # Latitude
    
    # ECI to ENU rotation matrix
    R = np.array([
        [-math.sin(lambda_),           math.cos(lambda_),           0          ],
        [-math.sin(phi)*math.cos(lambda_), -math.sin(phi)*math.sin(lambda_),  math.cos(phi)   ],
        [ math.cos(phi)*math.cos(lambda_),  math.cos(phi)*math.sin(lambda_),  math.sin(phi)   ]
    ])
    
    v_enu = R @ np.array([vx, vy, vz])
    return v_enu

def compute_heading_angle(r_eci, v_eci):
    """Compute heading angle from ECI position and velocity."""
    '''DO NOT USE THIS FUNCTION, IT IS NOT ACCURATE ENOUGH'''
    v_enu = eci_to_enu_velocity(r_eci, v_eci)
    v_east, v_north, v_up = v_enu
    
    heading = math.atan2(v_east, v_north)  # [-π, π]
    heading_deg = np.degrees(heading) % 360  # [0°, 360°]
    return heading_deg

def calculate_roll_angle(pitch_axis, roll_axis, gravity_vector):
    """
    计算航天器的滚转角（roll angle）。
    
    参数:\n
        pitch_axis: ECI坐标系下的pitch轴矢量 (3维数组)\n
        roll_axis: ECI坐标系下的roll轴矢量 (3维数组)\n
        gravity_vector: ECI坐标系下的重力矢量 (3维数组)\n
    
    返回:
        滚转角（弧度），范围 [-pi, pi]
    """
    '''DO NOT USE THIS FUNCTION, IT IS NOT ACCURATE ENOUGH'''
    roll_axis_normalized = roll_axis / np.linalg.norm(roll_axis)
    gravity_normalized = gravity_vector / np.linalg.norm(gravity_vector)
    
    up_direction = -gravity_normalized
    up_direction = up_direction - np.dot(up_direction, roll_axis_normalized) * roll_axis_normalized
    up_direction_normalized = up_direction / np.linalg.norm(up_direction)
    
    pitch_projection = pitch_axis - np.dot(pitch_axis, roll_axis_normalized) * roll_axis_normalized
    pitch_projection_normalized = pitch_projection / np.linalg.norm(pitch_projection)
    
    right_direction = np.cross(roll_axis_normalized, up_direction_normalized)
    right_direction_normalized = right_direction / np.linalg.norm(right_direction)
    
    roll_angle = np.arctan2(
        np.dot(pitch_projection_normalized, right_direction_normalized),
        np.dot(pitch_projection_normalized, up_direction_normalized)
    )
    
    return np.degrees(roll_angle) -90