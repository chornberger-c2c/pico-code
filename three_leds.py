#!/usr/bin/python

import machine
import utime

def switch(color, mode):
    if color == "red":
        pin = 15
    elif color == "yellow":
        pin = 14
    else:
        pin = 13
    machine.Pin(pin, machine.Pin.OUT).value(mode)
    utime.sleep(2)

while True:
    switch("red", 1)
    switch("red", 0)
    switch("yellow", 1)
    switch("yellow", 0)
    switch("green", 1)
    switch("green", 0)
    