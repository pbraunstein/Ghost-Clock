#!/usr/bin/env python
import pyautogui as p
from constants import *
import time
from sys import argv

def main():
    if len(argv) != 3:
        raise("Wrong number of arguments passed to ghost script")

    # Pull out args
    timeRegion = argv[1]
    numChimes = int(argv[2])

    if timeRegion == 'hour':
        hourChime(numChimes)
    elif timeRegion == 'fifteen':
        pass
    elif timeRegion == 'thirty':
        pass
    elif timeRegion == 'fortyfive':
        pass
    else:
        raise("Invalid time option passed to ghost script")


# Traces numChimes number of squares with the mouse
def hourChime(numChimes):
    p.moveTo(UL_X, UL_Y, duration=SWEEP_TIME)
    for x in range(numChimes):
        p.moveTo(UR_X, UR_Y, duration=SWEEP_TIME)
        p.moveTo(LR_X, LR_Y, duration=SWEEP_TIME)
        p.moveTo(LL_X, LL_Y, duration=SWEEP_TIME)
        p.moveTo(UL_X, UL_Y, duration=SWEEP_TIME)
        time.sleep(1)




if __name__ == '__main__':
    main()
