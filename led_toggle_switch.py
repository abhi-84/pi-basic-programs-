import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
switch_pin = 18
led_pin = 23
GPIO.setup(switch_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin,GPIO.OUT)

led_state=False
old_switch_state=True

while True:
	new_switch_state=GPIO.input(switch_pin)
	if new_switch_state == False and old_switch_state == True:
		led_state = not led_state
	old_switch_state=new_switch_state
	GPIO.output(led_pin,led_state)
	
