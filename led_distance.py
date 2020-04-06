# Adjust LED brightness based on distance from ultrasonic sensor

# GrovePi + Rotary Angle Sensor (Potentiometer) + LED
# http://www.seeedstudio.com/wiki/Grove_-_Rotary_Angle_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit


import time
import grovepi

# Connect the LED to digital port D5
led = 5
ultrasonic = 7
max_brightness = 255

grovepi.pinMode(led,"OUTPUT")
time.sleep(1)
i = 0

while True:
    try:
        # Read distance
        distance = grovepi.ultrasonicRead(ultrasonic)
        #print(distance)

        if (distance > 30):
            grovepi.analogWrite(led,0)
            print("too far away, setting off")
        else:
            # 255 = ON brightest
            # 0 = OFF
            # 0 - 30
            # 255 - 0
            distance_as_percentage = distance/30.0
            flipped_percentage = 1 - distance_as_percentage
            brightness = int(flipped_percentage * max_brightness)
            grovepi.analogWrite(led, brightness)
            print("setting brightness to ", brightness)

        # Send PWM signal to LED
        # 0 - 255
        #grovepi.analogWrite(led,i//4)

    except IOError:
        print("Error")