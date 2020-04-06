# LCD countdown display

from grovepi import *
from grove_rgb_lcd import *
import time

setRGB(0, 255, 0)

for x in range(10, 0, -1):
    setText("Time: %s" % x)
    time.sleep(1)

setText("Time's up!")
setRGB(255, 0, 0)

time.sleep(3)
setRGB(0,0,0)
setText("")
