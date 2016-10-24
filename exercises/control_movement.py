"""Simple exercise file where the kid must write code.

Control the LED light in the finch robot with this small exercise. The code
doesn't run as it is because a kid is supposed to complete the exercise first.
NAO will open this file in an editor.
"""

from exercises.finch.finch import Finch
from time import sleep

finch = Finch()


###############################################################################

# Write your code here. Your code defines the speed of the wheels and the
# duration of their movement

# CODE: rueda_izquierda = 0.5, rueda_derecha = 0, tiempo = 5
rueda_izquierda =
rueda_derecha =
tiempo =

###############################################################################

# Ahora pide al usuario que ingrese las velocidades
# rueda_izquierda = raw_input("Velocidad izquierda: ")
# rueda_derecha = raw_input("Velocidad derecha: ")

finch.wheels(rueda_izquierda, rueda_derecha)
sleep(tiempo)
finch.wheels(0, 0)
