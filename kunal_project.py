#!/usr/bin/python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN) #microphone
GPIO.setup(15,GPIO.OUT) #motor
while True:
    #GPIO.output(15,GPIO.LOW)
    print (GPIO.input(14))
    if GPIO.input(14) == 1:
        GPIO.output(15,GPIO.HIGH)
    if GPIO.input(14) == 0:
        GPIO.output(15,GPIO.LOW)
    

GPIO.cleanup()
