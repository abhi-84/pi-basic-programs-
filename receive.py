import serial
import time
ser=serial.Serial("/dev/ttyAMA0")
ser.baudrate=9600
while True:
	read=ser.read()
	print read
	time.sleep(.5)
