#!/usr/bin/env python
import pyautogui as p
import time
from sys import argv

def main():
    p.moveTo(100, 100, duration=0.75)
    for x in range(int(argv[1])):
        p.moveTo(1200, 100, duration=0.75)
        p.moveTo(1200, 800, duration=0.75)
        p.moveTo(100, 800, duration=0.75)
        p.moveTo(100, 100, duration=0.75)
        time.sleep(1)


if __name__ == '__main__':
    main()
