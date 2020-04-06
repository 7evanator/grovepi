# blink the lights as the countdown happens

import time
from grovepi import *
from grove_rgb_lcd import *

# lights
led_green = 5
led_red = 6
led_blue = 8

#buzzer
buzzer = 2

# set all the pinModes
pinMode(led_green,"OUTPUT")
pinMode(led_red,"OUTPUT")
pinMode(led_blue,"OUTPUT")
pinMode(buzzer,"OUTPUT")

# initialize the LCD screen
setRGB(0, 255, 0)
setText("")

# start the countdown
for i in range(10, 0, -1):
    setText("Time: %s" % i)
    analogWrite(led_green, 255)
    time.sleep(0.3)
    analogWrite(led_green, 0)
    analogWrite(led_blue, 255)
    time.sleep(0.3)
    analogWrite(led_blue, 0)
    analogWrite(led_red, 255)
    time.sleep(0.3)
    analogWrite(led_red, 0)
    digitalWrite(buzzer,1)
    time.sleep(0.1)
    digitalWrite(buzzer,0)

# set color to red and show final text
setText("Time's up!")
setRGB(255, 0, 0)
