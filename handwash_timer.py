# countdown time for washings hands
# triggered by the motion sensor


import time
from grovepi import *
from grove_rgb_lcd import *

# lights
led_green = 5
led_red = 6
led_blue = 8

# buzzer
buzzer = 2

# ultrasonic sensor
ultrasonic = 7

# global variable to track if the timer is running
timerRunning = False

# set all the pinModes
pinMode(led_green,"OUTPUT")
pinMode(led_red,"OUTPUT")
pinMode(led_blue,"OUTPUT")
pinMode(buzzer,"OUTPUT")

def doTimer():
    print("doTimer()")
    timerRunning = True
    setRGB(255, 0, 0)

    # start the countdown
    for i in range(20, 0, -1):
        setText("Time: %s" % i)
        analogWrite(led_green, 255)
        
        digitalWrite(buzzer,1)
        time.sleep(0.08)
        digitalWrite(buzzer,0)

        time.sleep(0.25)
        analogWrite(led_green, 0)
        analogWrite(led_blue, 255)
        time.sleep(0.24)
        analogWrite(led_blue, 0)
        analogWrite(led_red, 255)
        time.sleep(0.25)
        analogWrite(led_red, 0)

    # timer is done, show the "all done" message
    setRGB(0, 255, 0)
    setText("All clean!")
    digitalWrite(buzzer,1)
    time.sleep(1)
    digitalWrite(buzzer,0)
    time.sleep(2)
    resetDisplay()
    timerRunning = False

def resetDisplay():
    digitalWrite(buzzer,0)
    analogWrite(led_red, 0)
    analogWrite(led_green, 0)
    analogWrite(led_blue, 0)
    setRGB(0,0,0)
    setText("")

# initialize the LCD screen
resetDisplay()

# this is the main loop for the program
while True:
    try:
        distance = ultrasonicRead(ultrasonic)
        if (not timerRunning and distance > 0 and distance < 10):
            doTimer()

    except KeyboardInterrupt:
        # Reset everything when the script is interrupted
        resetDisplay()
        break
    except (IOError,TypeError) as e:
        # Print out the error message
        print("Error")


