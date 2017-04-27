# This program mimics a "Simon Says" type of game on the RPi using 3 LEDs
# and 3 Buttons corresponding to those LEDs.

import RPi.GPIO as GPIO
import time
from random import randint

green = 4
red = 17
yellow = 22
gButton = 18
rButton = 23
yButton = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(gButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(yButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

level = 1
sequence = []

# Creates a random sequence of length num, consisting of 3 colors
def create_sequence(num):
    seq = []
    for i in range(0,num):
        seq.append(getPin(randint(0,2)))
    return seq

# Gets the pin number for each random integer
def getPin(n):
    if n == 0:
        return green
    elif n == 1:
        return red
    else:
        return yellow

# Plays the random sequence on the LEDs
def play_sequence(lst):
    for n in lst:
        color = getPin(n)
        GPIO.output(color, 1)
        time.sleep(.2)
        GPIO.output(color, 0)
        time.sleep(.2)

def play_game(lev):
    sequence = create_sequence(lev)
    print "Playing sequence for level " + str(lev) + "..."
    play_sequence(sequence)
    current = 0
    color = sequence[0]
    while True:
        if current == len(sequence):
            return True
        else:
            color = sequence[current]
            if color == green:
                if not GPIO.input(gButton):
                    GPIO.output(green, 1)
                    time.sleep(0.2)
                    GPIO.output(green, 0)
                    current += 1
                    time.sleep(0.2)
                if not GPIO.input(rButton) or not GPIO.input(yButton):
                    return False
            if color == red:
                if not GPIO.input(rButton):
                    GPIO.output(red, 1)
                    time.sleep(0.2)
                    GPIO.output(red, 0)
                    current += 1
                    time.sleep(0.2)
                if not GPIO.input(gButton) or not GPIO.input(yButton):
                    return False
            if color == yellow:
                if not GPIO.input(yButton):
                    GPIO.output(yellow, 1)
                    time.sleep(0.2)
                    GPIO.output(yellow, 0)
                    current += 1
                    time.sleep(0.2)
                if not GPIO.input(gButton) or not GPIO.input(rButton):
                    return False


try:
    while True:
        print "Playing level..."
        if play_game(level):
            level += 1
        else:
            GPIO.output(green, 1)
            GPIO.output(red, 1)
            GPIO.output(yellow, 1)
            time.sleep(.2)
            GPIO.output(green, 0)
            GPIO.output(red, 0)
            GPIO.output(yellow, 0)
            quit()

except KeyboardInterrupt:
    GPIO.output(green, 0)
    GPIO.output(red, 0)
    GPIO.output(yellow, 0)
    GPIO.cleanup()
# rpiprojects
