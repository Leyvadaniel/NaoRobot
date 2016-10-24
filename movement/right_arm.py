"""Right arm movements.

Functions:
move_right -- move the right arm
"""
from naoqi.naoqi import *


def move_right(NAO_IP, PORT):
    """Move the right arm.

    Keyword arguments:
    NAO_IP -- Nao's IP
    PORT -- Port to connect to
    """
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([-1.31766, -1.31766, -1.31766, -1.31766])

    names.append("LElbowYaw")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([-0.52160, -0.52160, -0.52160, -0.52160])

    names.append("LHand")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([0.00443, 0.00443, 0.00443, 0.00443])

    names.append("LShoulderPitch")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([1.00933, 1.00933, 1.00933, 1.00933])

    names.append("LShoulderRoll")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([0.39266, 0.39266, 0.39266, 0.39266])

    names.append("LWristYaw")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([-1.52944, -1.52944, -1.52944, -1.52944])

    names.append("RElbowRoll")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([1.24258, 0.65275, 0.65275, 0.65275])

    names.append("RElbowYaw")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([0.51692, 0.51692, 0.51692, 0.51692])

    names.append("RHand")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([0.00525, 0.00525, 0.00525, 0.00525])

    names.append("RShoulderPitch")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([0.94805, 0.40492, -0.31940, 0.78191])

    names.append("RShoulderRoll")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([-0.31298, -0.47120, -0.92328, -0.00873])

    names.append("RWristYaw")
    times.append([0.50000, 1.00000, 2.00000, 3.50000])
    keys.append([-0.02305, -0.76271, 1.82387, 1.82387])

    try:
        motion = ALProxy("ALMotion", NAO_IP, PORT)
    except BaseException, err:
        print err

    motion.post.angleInterpolation(names, keys, times, True)
