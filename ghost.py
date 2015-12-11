#!/usr/bin/env python
import pyautogui as p
from constants import *
import time
from sys import argv

def main():
    if len(argv) != 3:
        raise Exception("Wrong number of arguments passed to ghost script")

    # Pull out args
    timeRegion = argv[1]

    try:
        numChimes = int(argv[2])
    except ValueError:
        numChimes = None

    if timeRegion == HOUR:
        hourChime(numChimes)
    elif timeRegion == FIFTEEN:
        fifteenChime()
    elif timeRegion == THIRTY:
        thirtyChime()
    elif timeRegion == FORTYFIVE:
        fortyfiveChime()
    else:
        raise Exception("Invalid time option passed to ghost script")


# Traces numChimes number of squares with the mouse
def hourChime(numChimes):
    p.moveTo(UL_X, UL_Y, duration=SWEEP_TIME)
    for x in range(numChimes):
        p.moveTo(UR_X, UR_Y, duration=SWEEP_TIME)
        p.moveTo(LR_X, LR_Y, duration=SWEEP_TIME)
        p.moveTo(LL_X, LL_Y, duration=SWEEP_TIME)
        p.moveTo(UL_X, UL_Y, duration=SWEEP_TIME)
        time.sleep(1)


# Traces a triangle on the screen with the mouse
def fifteenChime():
    p.moveTo(UM_X, UM_Y, duration=SWEEP_TIME)
    p.moveTo(LR_X, LR_Y, duration=SWEEP_TIME)
    p.moveTo(LL_X, LL_Y, duration=SWEEP_TIME)
    p.moveTo(UM_X, UM_Y, duration=SWEEP_TIME)


# Traces a horizontal line on the screen with the mouse
def thirtyChime():
    p.moveTo(ML_X, ML_Y, duration=SWEEP_TIME)
    p.moveTo(MR_X, MR_Y, duration=SWEEP_TIME)


def fortyfiveChime():
    p.moveTo(LM_X, LM_Y, duration=SWEEP_TIME)
    p.moveTo(UL_X, UL_Y, duration=SWEEP_TIME)
    p.moveTo(UR_X, UR_Y, duration=SWEEP_TIME)
    p.moveTo(LM_X, LM_Y, duration=SWEEP_TIME)



if __name__ == '__main__':
    main()
