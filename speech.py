"""Export long monologues for Nao.

Functions:
introduction -- Make Nao introduce itself.
"""

import time
from say import say


def introduction(tts):
    """Make Nao introduce itself.

    Keyword arguments:
    tts - Nao proxy.
    """
    say("Hello world!", tts)
    say("""I'm Leyva and I will teach you how to program in a programming
language called python""", tts)
    say("""Computer Science is one of the coolest subjects to study in the
modern world.""", tts)
    say("""Programming is a tool used by Scientists and Engineers to create
all kinds of interesting things.""", tts)
    say("""For example, you can program mobile phones, laptops, cars, the
Internet and more. Every day more things are being enhanced by
Artificial Intelligence, like me.""", tts)
    say("Now I want to talk about what programming is like.", tts)
    say("""Programming is about solving puzzles of the real world and helping
people deal with important problems to make the world a better
place.""", tts)

    time.sleep(2)
    say("""Now, what topic would you like to learn about? Show me a number to
choose the activity.""", tts)
    say("Number one to practice input and output.", tts)
