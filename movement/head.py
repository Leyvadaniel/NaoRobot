"""Head movements.

Functions:
yep -- nod the head
nope -- shake the head
"""
from naoqi import ALProxy


def yep(IP, PORT):
    """Nod the head.

    Keyword arguments:
    IP -- Nao's IP.
    PORT -- Port to connect to.
    """
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.40000, 0.80000, 1.20000, 1.60000, 2.00000])
    keys.append([-0.03993, -0.55501, 0.25831, -0.55501, -0.03993])

    names.append("HeadYaw")
    times.append([0.40000, 0.80000, 1.20000, 1.60000, 2.00000])
    keys.append([-0.03072, -0.03072, -0.03072, -0.03072, -0.03072])

    try:
        motion = ALProxy("ALMotion", IP, PORT)
        motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def nope(IP, PORT):
    """Shake the head.

    Keyword arguments:
    IP -- Nao's IP.
    PORT -- Port to connect to.
    """
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.40000, 0.80000, 1.20000, 1.60000])
    keys.append([-0.03993, -0.03993, -0.03993, -0.03993])

    names.append("HeadYaw")
    times.append([0.40000, 0.80000, 1.20000, 1.60000])
    keys.append([-0.03072, -0.96517, 0.86045, -0.03072])

    try:
        motion = ALProxy("ALMotion", IP, PORT)
        motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err
