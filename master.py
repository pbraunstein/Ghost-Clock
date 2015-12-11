#!/usr/bin/env python
import subprocess as sp
import os
from datetime import datetime
from constants import *


GHOST_SCRIPT = './ghost.py'

def main():
    timeSlice = datetime.now().time().minute
    reps = str(datetime.now().time().hour % 12)  # Mod to make it 12 hour
    if reps == '0':  # Manually make noon and midnight 12
        reps = '12'

    if timeSlice == 0:
        sp.Popen([GHOST_SCRIPT, HOUR, reps]) 
    elif timeSlice == 15:
        sp.Popen([GHOST_SCRIPT, FIFTEEN, '-'])  # reps only for hour
    elif timeSlice == 30:
        sp.Popen([GHOST_SCRIPT, THIRTY, '-'])
    elif timeSlice == 45:
        sp.Popen([GHOST_SCRIPT, FORTYFIVE, '-'])
    else:
        raise Exception("Invalid timeWord. Something likely wrong with when" +
                " Crontab starts master script")

if __name__ == '__main__':
    main()
