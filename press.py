#!/usr/bin/python

"""
light a led when a physical button is pressed
"""

import machine
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_external = machine.Pin(15, machine.Pin.OUT)
led_internal = machine.Pin(25, machine.Pin.OUT)

while True:
    if button.value() == 1:
        led_external.value(1)
        utime.sleep(1)
        led_external.value(0)
        led_internal.value(1)
        utime.sleep(1)
    led_internal.value(0)
    led_external.value(0)
