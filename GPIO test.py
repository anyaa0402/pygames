import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)

while True:
    GPIO.output(19,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(19,GPIO.LOW)
    time.sleep(0.5)
    
GPIO.cleanup()
