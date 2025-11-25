'''
Reading an analog heartbeat sensor

Basic heartbeat sensors use a green LED combined with a light sensor to read pulse
information through skin. This devices are very simple, outputing a value using an
analog signal.

To read the sensor, we can connect it to pin on a microcontroller that is capable
of reading analog values and turning them into digital values (an Analog-Digital
Convertor or ADC).

This code was written with the Rasperry Pi Pico in mind, but could be easily
adapted to other CircuitPython-compatible devices.
'''

# the board pin definitions, so we know what pins we have
import board
# time functions
import time

# analog pin reading module
from analogio import AnalogIn

# set up some constants and variables that we'll use later
DELAY_INTERVAL = 0.1 # when used with time.sleep, this is 1/10 of a second, or 10hz
ALPHA = 0.75

# set up the sensor pin for reading the heartbeat monitor
hbm_adc = AnalogIn(board.GP26)

previous = 0.0

# create an infinite runtime loop, where we'll read the sensor data and act on it
while True:
    #get the value from the hbm
    raw = hbm_adc.value
    # process the value
    processed = ALPHA * previous + (1 - ALPHA) * raw

    # print out the values
    print(f"{raw}, {processed}")
    # set the value to use for the next iteration of the loop
    previous = processed

    # wait for a bit before starting the loop again
    time.sleep(DELAY_INTERVAL)
