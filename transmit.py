import serial
import time
ser=serial.Serial("/dev/ttyAMA0")
ser.baudrate=9600
while True:
	ser.write("RAM ")
	time.sleep(.5)
