#!/usr/bin/python

import machine
import utime

pins = {
  "red": 15,
  "yellow": 14,
  "green": 13,
}

def switch(color, mode):
    turn = 1 if mode == "on" else 0
    machine.Pin(pins[color], machine.Pin.OUT).value(turn)
    utime.sleep(2)

while True:
    switch("red", "on")
    switch("red", "off")
    switch("yellow", "on")
    switch("yellow", "off")
    switch("green", "on")
    switch("green", "off")
