"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from audio import *

def checkLED():
    display.show("1")
    sleep(1000)

    image = Image("95159:"
                "69296:"
                "73937:"
                "89198:"
                "90909")
    display.show(image)
    sleep(1000)
    display.clear()


def checkButton():
    display.show("2")
    sleep(1000)

    button_a.was_pressed()
    button_b.was_pressed()

    while True:
        if (button_a.was_pressed()):
            sleep(1000)
            display.show(button_a.get_presses(), clear=False)
            sleep(1000)
            display.show(button_b.get_presses(), clear=False)
            return

def checkTemperature():
    display.show("3")
    sleep(1000)

    display.show(temperature())
    sleep(1000)
    display.clear()

def checkGesture():
    display.show("4")
    sleep(1000)

    while True:
        if (accelerometer.was_gesture('shake')):
            display.show("OK", clear=False)
            return

def checkAccelerometer():
    display.show("5")
    sleep(1000)

    while True:
        if accelerometer.get_x() > 500:
            display.show("L", clear=False)
            return

def checkTouchPin():
    display.show("0")
    sleep(1000)

    while True:
        if pin_logo.is_touched():
            display.show(Image.SURPRISED)
            return
""" def checkCompass():
    display.show("6")
    sleep(1000)

    compass.calibrate()

    while True:
        sleep(100)
        needle = ((15 - compass.heading()) // 30) % 12
        display.show(Image.ALL_CLOCKS[needle]) """

while True:
    # checkTouchPin()
    sleep(1000)
    checkLED()
    sleep(1000)
    checkButton()
    sleep(1000)
    checkTemperature()
    sleep(1000)
    checkGesture()
    sleep(1000)
    checkAccelerometer()
    # sleep(1000)
    # checkCompass()
    sleep(1000)
