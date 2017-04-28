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

def color(R, G, B, on_time):
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)
    time.sleep(on_time)

    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)

try:
    while True:
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    for i in range(0,101):
                        color((x*i),(y*i),(z*i), .02)

except KeyboardInterrupt:
    GPIO.cleanup()
