import time
import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,True)
time.sleep(random.randrange(1,8))
GPIO.output(4,False)
GPIO.cleanup()
