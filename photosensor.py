'''
Read the values from the photosensor monitor and use that to control the rate of blinking
on the Pico's built in LED
'''
import board
import time

from analogio import AnalogIn
from digitalio import  DigitalInOut

# set up the ADC for reading the photosensor
photosensor = AnalogIn(board.GP27)

# set up the LED on the PICO
led = DigitalInOut(board.LED)
led.switch_to_output()

delay = 0

# runtime loop, goes forever
while True:
    # read the value from the sensor
    value = photosensor.value
    # adjust value to be a reasonable amount of time!
    delay = value / 10000
    #print value to the serial console
    print(f"{value}, {delay}")
    # turn on the LED for a period of time controlled by the sensor read
    led.value = True
    time.sleep(delay)
    # turn off the LED for the same period of time
    led.value = False
    time.sleep(delay)
