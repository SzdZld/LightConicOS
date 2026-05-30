from JMOT import connect, extra
from typing import Literal

_TIME_SIGNALS = {
    'time_since_launch':220,
    'total_time':221,
    'frame_delta_time':222,
    'warp_amount':223,
    'real_time':224,
    'set_time_mode':40
}

def time_since_launch()->float:
    '''Get the time since the current vessel's launch in seconds.'''
    rec = connect._send_message(f"true<<{_TIME_SIGNALS['time_since_launch']}")
    return rec[0]
def total_time()->float:
    '''Get the total time since the start of the game in seconds.'''
    rec = connect._send_message(f"true<<{_TIME_SIGNALS['total_time']}")
    return rec[0]
def frame_delta_time()->float:
    '''Get the time elapsed since the last frame in seconds.'''
    rec = connect._send_message(f"true<<{_TIME_SIGNALS['frame_delta_time']}")
    return rec[0]
def warp_amount()->float:
    '''Get the current time warp factor.'''
    rec = connect._send_message(f"true<<{_TIME_SIGNALS['warp_amount']}")
    return rec[0]
def real_time()->float:
    '''Get the current real time since create of the game in seconds.'''
    rec = connect._send_message(f"true<<{_TIME_SIGNALS['real_time']}")
    return rec[0]
def set_time_mode(time_mode:Literal[-1,0,1,2,3,4,5,6,7,8,9,10,11,12]):
    '''
    time_mode:the time mode of the vessel,\n
        -1:0.05x\n
        0:pause\n
        1:normal\n
        2:fast(2x)\n
        3:10x\n
        4:25x\n
        5:100x\n
        6:500x\n
        7:2500x\n
        8:1W x\n
        9:5W x\n
        10:25W x\n
        11:100W x\n
        12:500W x\n
    '''
    ack = connect._send_message(f"false<<{_TIME_SIGNALS['set_time_mode']}<<{time_mode}")
    connect._verify(ack)