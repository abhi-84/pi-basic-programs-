import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #input pin is normally pulled up to 3.3V so after reading the input value, FALSE will be returned if switch is pressed
while True:
	input_state = GPIO.input(18)
	if input_state == False:
		print('Button Pressed')
		time.sleep(0.2)
