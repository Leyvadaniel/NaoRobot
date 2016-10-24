"""Export file monitoring functionality.

Classes:
FileMonitor -- monitor file changes and react
"""

import os
import time

from parser import parse
from say import say


class FileMonitor:
    """Monitor if a file changes and react to it by speaking."""

    def setData(self, fileName, lines, strings):
        """Set all the monitoring data.

        Keyword arguments:
        fileName -- complete path of the file to monitor
        lines -- a list containing all the lines to check
        strings -- a list containing all the right answers to the previous
        lines
        """
        self.FILE_NAME = fileName
        self.LINES = lines
        self.STRINGS = strings

    def read_stamp(self):
        """Return the time stamp of the last modification of the file."""
        return os.stat(self.FILE_NAME).st_mtime

    def wait_and_read(self):
        """Wait a fixed time and return the modification time stamp."""
        time.sleep(1)
        return self.read_stamp()

    def monitor_file(self, tts):
        """Wait for a modification, call the parser and give feedback.

        Start monitoring a file and when a change in its modified time stamp is
        detected, call the parser to check if there's a line where the kid made
        a mistake. Afterwards, give the kid the line number or his/her program
        running as a reward
        Keyword arguments:
        tts -- Nao proxy used to make it speak
        """
        exercise_completed = False

        # get initial modification time stamp
        past_stamp = self.read_stamp()

        while not exercise_completed:
            new_stamp = self.wait_and_read()

            # keep waiting for the time stamp to change
            while new_stamp == past_stamp:
                new_stamp = self.wait_and_read()

            past_stamp = new_stamp

            # get the faulty line from the parser or None if it's correct
            faulty_line = parse(self.FILE_NAME, self.LINES, self.STRINGS)

            if faulty_line is None:
                # Run the monitored file so the child can see it working
                say('Good job! The program was executed successfully', tts)
                execfile(self.FILE_NAME)
                exercise_completed = True
            else:
                say('Oops! Error on line ' + str(faulty_line) + '. Remember, you have to complete the code that appears in line 20 by using the code that appears commented in line 19 as reference. After that, you will assign one of the available colors to the FINCH, which you consult on the line that starts with the word "switcher"', tts)
