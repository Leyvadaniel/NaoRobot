"""Define functionality to be called by Nao when it detects a number"""

from naoqi.naoqi import ALModule

nextExercise = None

class Callback(ALModule):
    """Create a module to be recognized by the main flow"""
    def pictureChanged(self, strVarName, value, strMessage):
        pictureChanged(strVarName, value, strMessage)
            
def pictureChanged(strVarName, value, strMessage):        
    """Actual function called by the main flow as the official docs state"""
    try:
        global nextExercise
        nextExercise = value[1][0][0][1]
    except IndexError:
        pass
