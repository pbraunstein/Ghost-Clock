#!/usr/bin/env python
import subprocess as sp
import os
from datetime import datetime

GHOST_SCRIPT = os.path.join(os.getcwd(), 'ghost.py')

def main():
    reps = str(datetime.now().time().hour % 12)  # Mod to make it 12 hour

    sp.Popen([GHOST_SCRIPT, reps]) 

if __name__ == '__main__':
    main()
