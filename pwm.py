import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
pwm=GPIO.PWM(13,50)
pwm.start(0)
while True:
    for i in range(0,100,10):		 	
        pwm.ChangeDutyCycle(i)	# motor rotates from 0 to 99 due to change in duty cycle, by i
        GPIO.output(13,True)
	time.sleep(0.1)		# wait 0.1 sec
    for i in range(100, 0,-10):	# decrement the duty cycle (-1)
	pwm.ChangeDutyCycle(i)
	GPIO.output(13,True)
	time.sleep(0.1)

