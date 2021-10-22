#!/usr/bin/python

"""
go through all pins on Pi Pico to identify which led corresponds to which pin
"""

import machine
import utime

for i in range(30):
    led = machine.Pin(i, machine.Pin.OUT)
    led.toggle()
    print("led: ", i)
    utime.sleep(1)
    led.toggle()
