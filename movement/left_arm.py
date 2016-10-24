# -*- coding: utf-8 -*-
"""Left arm movements.

Functions:
move_left -- move the left arm
"""
from naoqi.naoqi import *

# Choregraphe simplified export in Python.


def move_left(NAO_IP, PORT, wait_id):
    """Move the left arm.

    Keyword arguments:
    NAO_IP -- Nao's IP
    PORT -- Port to connect to
    """
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([ 0.80000, 2.00000, 3.40000])
    keys.append([ -0.40476, -0.62483, -1.33867])
    
    names.append("LElbowYaw")
    times.append([ 0.80000])
    keys.append([ -1.18597])
    
    names.append("LHand")
    times.append([ 0.80000, 1.32000, 2.00000, 3.40000])
    keys.append([ 0.00524, 0.00733, 0.01257, 0.00419])
    
    names.append("LShoulderPitch")
    times.append([ 0.80000, 1.32000, 2.00000, 3.40000])
    keys.append([ 1.49933, 0.52185, -0.14486, 1.18682])
    
    names.append("LShoulderRoll")
    times.append([ 0.80000, 2.00000, 3.40000])
    keys.append([ 0.15019, 0.89361, 0.31241])
    
    names.append("LWristYaw")
    times.append([ 0.80000, 2.00000, 3.40000])
    keys.append([ 0.10059, -1.82387, -1.49226])
    
    names.append("RElbowRoll")
    times.append([ 0.80000])
    keys.append([ 0.40415])
    
    names.append("RElbowYaw")
    times.append([ 0.80000])
    keys.append([ 1.18639])
    
    names.append("RHand")
    times.append([ 0.80000])
    keys.append([ 0.00524])
    
    names.append("RShoulderPitch")
    times.append([ 0.80000])
    keys.append([ 1.49941])
    
    names.append("RShoulderRoll")
    times.append([ 0.80000])
    keys.append([ -0.15191])
    
    names.append("RWristYaw")
    times.append([ 0.80000])
    keys.append([ 0.09931])
    
    try:
        motion = ALProxy("ALMotion", NAO_IP, PORT)
        motion.wait(wait_id, 0)
        motion.post.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err
