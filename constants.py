#!/usr/bin/env python
from Quartz import CGDisplayBounds
from Quartz import CGMainDisplayID

# Get screen bounds
infos = CGDisplayBounds(CGMainDisplayID())
w = infos.size.width
h = infos.size.height

# Screen location constants
OFF  = 100
UL_X = OFF
UL_Y = OFF
UR_X = w - OFF
UR_Y = OFF
LR_X = w - OFF
LR_Y = h - OFF
LL_X = OFF
LL_Y = h - OFF

# Time constants
SWEEP_TIME = 0.75
HOUR = 'hour'
FIFTEEN = 'fifteen'
THIRTY = 'thirty'
FORTYFIVE = 'fortyfive'



