import math
import numpy as np

import numpy as np

def eci2ecef(r_eci, total_seconds):
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
    lon_rad = np.radians(lon)
    lat_rad = np.radians(lat)
    X = (R + h) * np.cos(lat_rad) * np.cos(lon_rad)
    Y = (R + h) * np.cos(lat_rad) * np.sin(lon_rad)
    Z = (R + h) * np.sin(lat_rad)
    return np.array([X, Y, Z])


def ecef2enu(lon, lat, v_ECEF):
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
    heading = np.degrees(np.arctan2(v_e, v_n))
    
    norm = np.sqrt(v_e**2 + v_n**2 + v_u**2)
    pitch = np.degrees(np.arcsin(v_u / norm))
    
    return pitch, heading


def eci_to_enu_velocity(r_eci, v_eci):
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
    v_enu = eci_to_enu_velocity(r_eci, v_eci)
    v_east, v_north, v_up = v_enu
    
    heading = math.atan2(v_east, v_north)  # [-π, π]
    heading_deg = np.degrees(heading) % 360  # [0°, 360°]
    return heading_deg

def calculate_roll_angle(pitch_axis, roll_axis, gravity_vector):
    """
    计算航天器的滚转角（roll angle）。
    
    参数:
        pitch_axis: ECI坐标系下的pitch轴矢量 (3维数组)
        roll_axis: ECI坐标系下的roll轴矢量 (3维数组)
        gravity_vector: ECI坐标系下的重力矢量 (3维数组)
    
    返回:
        滚转角（弧度），范围 [-pi, pi]
    """
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