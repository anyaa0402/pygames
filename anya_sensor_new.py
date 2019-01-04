import RPi.GPIO as GPIO
import time
import pygame

pygame.mixer.init()
first = pygame.mixer.Sound("click_one.wav")
first.set_volume(10)
##second = pygame.mixer.Sound("")
##third = pygame.mixer.Sound("")
##fourth = pygame.mixer.Sound("")

GPIO.setmode(GPIO.BCM)
trigger = 14
echo = 15
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21,GPIO.IN)
GPIO.output(trigger, GPIO.LOW)
time.sleep(2)

while True:
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
        t=distance/50
        print (t)
        print ("Distance:" , distance , "cm.")

        if distance <= 25 :
                first.play()
                time.sleep(t)
##      while distance <= 15 and distance > 10:
##              second.play()
##              break
##      while distance <=10 and distance > 5:
##              third.play()
##              break
##      while distance <=5 and distance > 0:
##              fourth.play()
##              break

GPIO.cleanup()
