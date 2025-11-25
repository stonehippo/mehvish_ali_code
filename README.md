# Code for Mehvish

A collection of code examples using [CircuitPython](https://circuitpython.org), a [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/), and the [Elegoo Sensor Kit](https://www.elegoo.com/blogs/arduino-projects/elegoo-37-in-1-sensor-modules-kit-tutorial).

These examples are adapted from the Arduino code provided by Elegoo for use with the sensors from the kit.

# Development Tools

For some general documentation on the Pico dev board and CircuitPython, this [Adafruit guide](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython) is a good place to start. It has a lot of code and wiring examples that can help you get started. I recommend reading through it and perhaps trying some of the examples before embarking on deeper work.

In addition to the hardware—the Pico dev board, the sensors, a breadboard, and some wires to connect them—you will need a text editor to edit the files on the Pico. This is best done with a code-specific editor or an integrated development environment (IDE).

I recommend using [Thonny](https://thonny.org/). It is a simple, free, Python-focused IDE that has some built in tools for working with CircuitPython. This includes handy things like:

- a REPL (read-eval-print-loop) view that makes quick hacks and code output easy
- a plotter for visualizing numeric data from a sensor or device
- coding tools like object inspectors and autocomplete

# Code Examples

- [hearbeat monitor](./heartbeat.py)
- [photo sensor](./photosensor.py)
