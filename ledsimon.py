import RPi.GPIO as GPIO
import time

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

try:
    while True:
        if(GPIO.input(gButton)):
            print 'Green pressed'
            GPIO.output(green, 1)
            time.sleep(1)
            GPIO.output(green, 0)
        if(GPIO.input(rButton)):
            print 'Red pressed'
            GPIO.output(red, 1)
            time.sleep(1)
            GPIO.output(red, 0)
        if(GPIO.input(yButton)):
            print 'Yellow pressed'
            GPIO.output(yellow,1)
            time.sleep(1)
            GPIO.output(yellow,1)
except KeyboardInterrupt:
    GPIO.output(green, 0)
    GPIO.output(red, 0)
    GPIO.output(yellow, 0)
    GPIO.cleanup()
# rpiprojects
