import RPi.GPIO as GPIO
import time

red = 4
green = 17
blue = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100

RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)

try:
    while True:
        print "red"
        for r in range(0,101):
            RED.ChangeDutyCycle(r)
            time.sleep(.02)
        print "green"
        for g in range(0,101):
            GREEN.ChangeDutyCycle(g)
            time.sleep(.02)
        print "blue"
        for b in range(0,101):
            BLUE.ChangeDutyCycle(b)
            time.sleep(.02)

except KeyboardInterrupt:
    GPIO.cleanup()
