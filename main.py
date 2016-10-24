"""Main program for the nao classroom."""

# -*- coding: utf-8 -*-
from naoqi.naoqi import ALProxy
from naoqi.naoqi import ALModule
from naoqi.naoqi import ALBroker
from FileMonitor import FileMonitor
from speech import introduction
from say import say
from movement.left_arm import move_left
from movement.right_arm import move_right


import time
from subprocess import Popen

import Callback


NAO_IP = '10.17.12.128'
PC_IP = '10.15.92.237'
PORT = 9559
EDITOR_NAME = 'gedit'


def main():
    """Entry point for the program."""
    tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    ascii_art = """
==================================================================
      ___       ___           ___           ___           ___     
     /\__\     /\  \         |\__\         /\__\         /\  \    
    /:/  /    /::\  \        |:|  |       /:/  /        /::\  \   
   /:/  /    /:/\:\  \       |:|  |      /:/  /        /:/\:\  \  
  /:/  /    /::\~\:\  \      |:|__|__   /:/__/  ___   /::\~\:\  \ 
 /:/__/    /:/\:\ \:\__\     /::::\__\  |:|  | /\__\ /:/\:\ \:\__\ 
 \:\  \    \:\~\:\ \/__/    /:/~~/~     |:|  |/:/  / \/__\:\/:/  /
  \:\  \    \:\ \:\__\     /:/  /       |:|__/:/  /       \::/  / 
   \:\  \    \:\ \/__/     \/__/         \::::/__/        /:/  /  
    \:\__\    \:\__\                      ~~~~           /:/  /   
     \/__/     \/__/                                     \/__/    

==================================================================="""
    print bcolors.BOLD + bcolors.OKGREEN + ascii_art

    id_ = stand(NAO_IP)
    move_left(NAO_IP, PORT, id_)
    move_right(NAO_IP, PORT)
    introduction(tts)
    sit(NAO_IP)

    nextExercise = ''

    while(nextExercise != 'Zero'):
        nextExercise = getNextExercise()

        say('You selected number '+nextExercise, tts)
        if nextExercise == 'One':
            move_left(NAO_IP, PORT, id_)
            move_right(NAO_IP, PORT)
            say("""An input is the information that is inserted into a program
by an user. This information can take many forms: it can be
something simple like text that was typed on the keyboard or it
can be something more complex, like the image I just read a
while ago.""", tts)
            move_left(NAO_IP, PORT, id_)
            move_right(NAO_IP, PORT)
            say("""The input is used and manipulated by the computer in order
to do different things, like making a calculation, accelerate a
car, or even make a videogame character attack. These all would
be  outputs, which can be defined as the information provided
by a computer or program.""", tts)
            move_left(NAO_IP, PORT, id_)
            move_right(NAO_IP, PORT)
            say("""In this exercise you want to change the color of my friend
FINCH. The code you will work with is already half done, but it
is still missing the instruction that asks the user to input
the value of the color that they want to assign to FINCH""",
                tts)
            time.sleep(2)
            move_left(NAO_IP, PORT, id_)
            move_right(NAO_IP, PORT)
            say("""To do this, you have to complete the code that appears in line
20 by using the code that appears commented in line 19 as
reference. After that, you will assign one of the available
colors to the FINCH""", tts)
            startLesson('exercises/control_leds.py',
                        [20],
                        ["color = raw_input('color:')"],
                        tts,
                        EDITOR_NAME)
        elif nextExercise == 'Two':
            startLesson('exercises/control_movement.py',
                        [20, 21, 22],
                        ["rueda_izquierda = 0.5",
                         "rueda_derecha = 0",
                         "tiempo = 5"],
                        tts,
                        EDITOR_NAME)
        elif nextExercise == 'Zero':
            say('Goodbye!', tts)
        else:
            say('That number is not assigned to any lesson', tts)


def startLesson(fileName, lineList, stringList, tts, editorName):
    """Create a FileMonitor, open an editor and monitor file.

    Keyword arguments:
    fileName -- file to monitor and open
    lineList -- list of lines to monitor
    stringList -- list of correct lines
    tts -- Nao proxy
    editorName -- Editor to open for the kid
    """
    monitor = FileMonitor()
    monitor.setData(fileName, lineList, stringList)
    openEditor(editorName, fileName)
    monitor.monitor_file(tts)


def openEditor(editorName, fileName):
    """Open a selected editor.

    Keyword arguments:
    editorName -- editor to open
    fileName -- file to open
    """
    Popen(editorName + " " + fileName, shell=True)


def getNextExercise():
    """

    """
    Callback.nextExercise = None

    moduleName = "Callback"
    memValue = "PictureDetected"

    recoProxy = ALBroker("pythonBroker", PC_IP, 0, NAO_IP, PORT)
    pythonModule = Callback.Callback(moduleName)

    # Create a proxy to ALMemory
    try:
        memoryProxy = ALProxy("ALMemory", NAO_IP, PORT)
    except RuntimeError, e:
        print "Error when creating ALMemory proxy:", e
        exit(1)

    # Have the python module called back when picture recognition results
    # change.
    try:
        memoryProxy.subscribeToEvent(memValue, moduleName, "pictureChanged")
    except RuntimeError, e:
        print "Error when subscribing to micro event"
        exit(1)

    # Let the picture recognition run for a little while (will stop after
    # 'count' calls of the callback).
    # You can check the results using a browser connected on your Nao, then
    # Advanced -> Memory -> type PictureDetected in the field
    while Callback.nextExercise is None:
        time.sleep(1)

    # unsubscribe modules
    memoryProxy.unsubscribeToEvent(memValue, moduleName)

    return Callback.nextExercise


def StiffnessOn(proxy):
    """Turn stiffness on.

    Keyword arguments:
    proxy -- Nao proxy
    """    
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def stand(robotIP):
    """Make Nao stand.

    Warning: Needs a PoseInit before executing
    Keyword arguments:
    robotIP -- Nao's IP
    """
    # Init proxies.
    motionProxy = ALProxy("ALMotion", robotIP, 9559)

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)

    # Send NAO to Pose Init
    return postureProxy.post.goToPosture("StandInit", 0.5)


def sit(robotIP):
    """Make Nao stand.

    Warning: Needs a PoseInit before executing
    Keyword arguments:
    robotIP -- Nao's IP
    """
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    postureProxy.goToPosture("Sit", 0.5)


if __name__ == "__main__":
    main()
