#!/usr/bin/python

"""
control a sequence of led lights on the Rasperry Pi Pico (turned on or off)
"""

import machine
import utime

# assign each color of led to its pin number
pins = {
    "red": 15,
    "yellow": 14,
    "green": 13,
}

def switch(color, mode):
    """
    switch a led with a certain color on or off
    """
    turn = 1 if mode == "on" else 0
    machine.Pin(pins[color], machine.Pin.OUT).value(turn)
    utime.sleep(2)

# do the loop sequence
while True:
    switch("red", "on")
    switch("red", "off")
    switch("yellow", "on")
    switch("yellow", "off")
    switch("green", "on")
    switch("green", "off")
