#!/usr/bin/env python
from Quartz import CGDisplayBounds
from Quartz import CGMainDisplayID

# Get screen bounds
infos = CGDisplayBounds(CGMainDisplayID())
w = infos.size.width
h = infos.size.height

# Screen corner constants
OFF  = 100
UL_X = OFF
UL_Y = OFF
UR_X = w - OFF
UR_Y = OFF
LR_X = w - OFF
LR_Y = h - OFF
LL_X = OFF
LL_Y = h - OFF

# Middle of screen constants
UM_X = int(round((float(UL_X) + float(UR_X)) / 2))
UM_Y = OFF
ML_X = OFF
ML_Y = int(round((float(UL_Y) + float(LL_Y)) / 2))
MR_X = w - OFF
MR_Y = int(round((float(UL_Y) + float(LL_Y)) / 2))
LM_X = int(round((float(LL_X) + float(LR_X)) / 2))
LM_Y = h - OFF

# Time constants
SWEEP_TIME = 0.75
HOUR = 'hour'
FIFTEEN = 'fifteen'
THIRTY = 'thirty'
FORTYFIVE = 'fortyfive'



