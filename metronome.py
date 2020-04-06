# metronome -- buzz a buzzer at a repeated interval based on the rotary dial (potentiometer)

import time
import grovepi


# Connect the Rotary Angle Sensor to analog port A2
potentiometer = 2

# Connec the buzzer to port D2
buzzer_pin = 2

# Assign mode for buzzer as output
grovepi.pinMode(buzzer_pin,"OUTPUT")


intervals = [0.25, 0.5, 0.75, 1.0]

buzzer_length = 0.1

while True:
    try:
        # Read resistance from Potentiometer
        i = grovepi.analogRead(potentiometer)
        # i will be between 0 and 1023 (inclusive)
        interval = intervals[i//256]
        print(interval)

        grovepi.digitalWrite(buzzer_pin,1)
        time.sleep(buzzer_length)
        grovepi.digitalWrite(buzzer_pin,0)
        time.sleep(interval)

    except KeyboardInterrupt:   # Stop the buzzer before stopping
        grovepi.digitalWrite(buzzer_pin,0)
        break
    except (IOError,TypeError) as e:
        print("Error")