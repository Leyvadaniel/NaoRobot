"""Simple exercise file where the kid must write code.

Control the LED light in the finch robot with this small exercise. The code
doesn't run as it is because a kid is supposed to complete the exercise first.
NAO will open this file in an editor.
"""

from exercises.finch.finch import Finch
from time import sleep

finch = Finch()
switcher = {'blue': '#0000FF', 'yellow': '#FFFF00', 'green': '#008000'}

###############################################################################

# Write your code here. Your code asks the user for a color from the ones
# defined above

# CODE: color = raw_input('color:')
color = raw_input('color:')

###############################################################################

colorIsValid = False


finchColor = switcher.get(color)

while(finchColor is None):
    print('Invalid color. Valid colors are: ' + ', '.join(switcher.keys()))
    finchColor = switcher.get(raw_input('color:'))


finch.led(finchColor)

sleep(5)
