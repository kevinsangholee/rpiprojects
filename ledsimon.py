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

def create_sequence(num):
    sequence = []
    for i in range(0,num):
        sequence.append(randint(0,2))

def getPin(n):
    if n == 0:
        return green
    elif n == 1:
        return red
    else:
        return yellow

def play_sequence(lst):
    for n in lst:
        GPIO.output(getPin(n), 1)
        time.sleep(.2)
        GPIO.output(getPin(n), 0)
        time.sleep(.2)

try:
    while True:
        print "Playing sequence..."
        time.sleep(2)
        create_sequence(3)
        play_sequence(sequence)

        """if(not GPIO.input(gButton)):
            print 'Green pressed'
            GPIO.output(green, 1)
            time.sleep(1)
            GPIO.output(green, 0)
        if(not GPIO.input(rButton)):
            print 'Red pressed'
            GPIO.output(red, 1)
            time.sleep(1)
            GPIO.output(red, 0)
        if(not GPIO.input(yButton)):
            print 'Yellow pressed'
            GPIO.output(yellow,1)
            time.sleep(1)
            GPIO.output(yellow,0)"""
except KeyboardInterrupt:
    GPIO.output(green, 0)
    GPIO.output(red, 0)
    GPIO.output(yellow, 0)
    GPIO.cleanup()
# rpiprojects
