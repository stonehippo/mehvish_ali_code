# Code for Mehvish

A collection of code examples using a couple of different microcontrollers.

In the [curcuitpython directory](./circuitpython), there are eamples using [CircuitPython](https://circuitpython.org), a [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/), and the [Elegoo Sensor Kit](https://www.elegoo.com/blogs/arduino-projects/elegoo-37-in-1-sensor-modules-kit-tutorial).

In the [arduino directory](./arduino/), there are matching examples using the same Elegoo sensors, but this time written in [Arduino](https://arduino.cc) and using an [Arduino Uno R3](https://store.arduino.cc/products/arduino-uno-rev3) dev board.

These examples are adapted from the Arduino code provided by Elegoo for use with the sensors from the kit.

## Development Tools for CircuitPython

For some general documentation on the Pico dev board and CircuitPython, this [Adafruit guide](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython) is a good place to start. It has a lot of code and wiring examples that can help you get started. I recommend reading through it and perhaps trying some of the examples before embarking on deeper work.

In addition to the hardware—the Pico dev board, the sensors, a breadboard, and some wires to connect them—you will need a text editor to edit the files on the Pico. This is best done with a code-specific editor or an integrated development environment (IDE).

I recommend using [Thonny](https://thonny.org/). It is a simple, free, Python-focused IDE that has some built in tools for working with CircuitPython. This includes handy things like:

- a REPL (read-eval-print-loop) view that makes quick hacks and code output easy
- a plotter for visualizing numeric data from a sensor or device
- coding tools like object inspectors and autocomplete

## Development Tools for Arduino

The Arduino IDE is the most common way to write, test, and deploy code for Arduino devices. It is available [here](https://www.arduino.cc/en/software/#ide).

## Code Examples

### CircuitPython

- [hearbeat monitor](./circuitpython/heartbeat.py)
- [photo sensor](./circuitpython/photosensor.py)

### Arduino

- [heartbeat monitor](./arduino/heartbeat/)
- [photo sensor](./arduino/photosensor/)

## Additional Resources

pulsesensor.com has a lot of useful [Arduino examples for working with a pulse sensor](https://pulsesensor.com/pages/installing-our-playground-for-pulsesensor-arduino). I recommend checking those out if you want to see some advanced ideas for working with the sensor. The code is easy to read and should be easy enough to adapt to CircuitPython or another language.

There is also an Adafruit guide for[ working with a pulse sensor and CircuitPython](https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython/pulse). This guide is for a different sensor, but the concepts and code are pretty much universal. It also makes use of the now-defunct Mu Editor, but no worries, Thonny has the same functionality. 
