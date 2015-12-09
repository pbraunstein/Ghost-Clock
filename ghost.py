#!/usr/bin/env python
import pyautogui as p
import time

p.moveTo(100, 100, duration=0.75)
while True:
    p.moveTo(1200, 100, duration=0.75)
    p.moveTo(1200, 800, duration=0.75)
    p.moveTo(100, 800, duration=0.75)
    p.moveTo(100, 100, duration=0.75)
    time.sleep(1)
