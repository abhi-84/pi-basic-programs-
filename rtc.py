#importing header file for i2c and time
import smbus
import time
#Address artt which DS1307 RTC is connected to raspberry
addr=0x68
#smbus defination to use i2c bus
b=smbus.SMBus(1)
#Writing a byte i.e. data write mode - slave receiver mode
#(0xd0 for RTC1307) for DS1307 RTC
b.write_byte(0x68,0xd0)
def rtc1307():
# Initializing DS1307 RTC for Second, Minute, Hour, Day, Date, Month, Year
	b.write_byte_data(0x68,0x00,0x52) #Second register with 0x52 initial value
	b.write_byte_data(0x68,0x01,0x37) #Minute register with 0x55 initial value
	b.write_byte_data(0x68,0x02,0x21) #Hour register with 0x38 initial value
	b.write_byte_data(0x68,0x03,0x04) #Day register with 0x03 initial value
	b.write_byte_data(0x68,0x04,0x29) #Date register with 0x04 initial value
	b.write_byte_data(0x68,0x05,0x09) #Month register with 0x03 initial value
	b.write_byte_data(0x68,0x06,0x16) #Year register with 0x05 initial value

def readRTC1307():
# Reading DS1307 RTC for Second, Minute, Hour, Day, Date, Month, Year
	r0=b.read_byte_data(0x68,0x00)
	r1=b.read_byte_data(0x68,0x01)
	r2=b.read_byte_data(0x68,0x02)
	r3=b.read_byte_data(0x68,0x03)
	r4=b.read_byte_data(0x68,0x04)
	r5=b.read_byte_data(0x68,0x05)
	r6=b.read_byte_data(0x68,0x06)
#Conversiong from BCD to decimal
	sec=(r0&0x0f)+((r0 &0xf0)>>4)*10
	minu=(r1 & 0x0f)+((r1 & 0xf0)>>4)*10
	hour=(r2 & 0x0f)+((r2 & 0xf0)>>4)*10
	day=(r3 & 0x0f)+((r3 & 0xf0)>>4)*10
	date=(r4 & 0x0f)+((r4 & 0xf0)>>4)*10
	month=(r5 & 0x0f)+((r5 & 0xf0)>>4)*10
	year=(r6 & 0x0f)+((r6 & 0xf0)>>4)*10
#Printing the values on terminal of python
	print "Time:",hour,"/",minu,"/",sec,"\n"
	print "Week day is:",day,"\n"
	print "Date is:","0"+str(date),"/","0"+str(month),"/",year,"\n"
#Initialization function for RTC1307

rtc1307()
#Writing a byte i.e. data read mode - slave transmit mode
#(0xd1 for RTC1307) for DS1307 RTC
b.write_byte(0x68,0xd1)

while True:
	readRTC1307()
	print "Waiting to read RTC1307\n"
	time.sleep(1)
