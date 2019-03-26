import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.IN)
while True:
    x=GPIO.input(15)
    if x==True:
        GPIO.output(13,True)
        time.sleep(1)
        GPIO.output(13,False)
        time.sleep(1)
    else:
        GPIO.output(13,True)            

