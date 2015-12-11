#!/usr/bin/env python
import subprocess as sp
import os
from datetime import datetime
from constants import *


GHOST_SCRIPT = './ghost.py'

def main():
    timeSlice = datetime.now().time().minute
    reps = str(datetime.now().time().hour % 12)  # Mod to make it 12 hour

    if timeSlice == 15:
        sp.Popen([GHOST_SCRIPT, FIFTEEN, None])  # reps only for hour
    elif timeSlice == 30:
        sp.Popen([GHOST_SCRIPT, THIRTY, None])
    elif timeSlice == 45:
        sp.Popen([GHOST_SCRIPT, FORTYFIVE, None])
    elif timeSlice == 0:
        sp.Popen([GHOST_SCRIPT, HOUR, reps]) 
    else:
        raise("Invalid timeWord. Something likely wrong with when" +
                " Crontab starts master script")

if __name__ == '__main__':
    main()
