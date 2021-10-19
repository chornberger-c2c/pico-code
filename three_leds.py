#!/usr/bin/python

import machine
import utime

def switch(color, mode):
    if mode == "on":
        turn = 1
    elif mode == "off":
        turn = 0
    if color == "red":
        pin = 15
    elif color == "yellow":
        pin = 14
    elif color == "green":
        pin = 13

    machine.Pin(pin, machine.Pin.OUT).value(turn)
    utime.sleep(2)

while True:
    switch("red", "on")
    switch("red", "off")
    switch("yellow", "on")
    switch("yellow", "off")
    switch("green", "on")
    switch("green", "off")