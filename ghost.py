#!/usr/bin/env python
import pyautogui as p
import time
from sys import argv
from Quartz import CGDisplayBounds
from Quartz import CGMainDisplayID

# Constants
OFF  = 100

def main():
    # Get screen bounds
    infos = CGDisplayBounds(CGMainDisplayID())
    w = infos.size.width
    h = infos.size.height

    # Calculate corners
    UL_X = OFF
    UL_Y = OFF
    UR_X = w - OFF
    UR_Y = OFF
    LR_X = w - OFF
    LR_Y = h - OFF
    LL_X = OFF
    LL_Y = h - OFF

    p.moveTo(UL_X, UL_Y, duration=0.75)
    for x in range(int(argv[1])):
        p.moveTo(UR_X, UR_Y, duration=0.75)
        p.moveTo(LR_X, LR_Y, duration=0.75)
        p.moveTo(LL_X, LL_Y, duration=0.75)
        p.moveTo(UL_X, UL_Y, duration=0.75)
        time.sleep(1)


if __name__ == '__main__':
    main()
