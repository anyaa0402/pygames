import RPi.GPIO as GPIO
import time
import pygame
GPIO.setmode(GPIO.BCM)
trigger = 14
echo = 15
##s = Sound()
##s.read('doublebass.wav')
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21,GPIO.IN)
on=0
GPIO.output(trigger, GPIO.LOW)
time.sleep(2)
while True:
    #=GPIO.input(21)
    #print(x)
    
    #if x == 0: #button pressed
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(trigger, GPIO.LOW)

    while GPIO.input(echo) == 0:
        start = time.time()
    while GPIO.input(echo) == 1:
        end = time.time()

    duration = end - start
    distance = duration*17150
    distance = round(distance,2)
    print ("Distance:" , distance , "cm.")

    if distance <= 20:
        GPIO.output(18,GPIO.HIGH)
##        s.play()
    else:
        GPIO.output(18,GPIO.LOW)

GPIO.cleanup()
