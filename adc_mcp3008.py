#import header files
import spidev
import time
#calling SPI development files
spi=spidev.SpiDev()
#spi.open(0,0)
#Function to read ADC value with channel number as argument
def analog_read(channel):
	r=spi.xfer2([1,(8+channel)<<4,0])
	adc_out=((r[1]&3)<<8)+r[2]
	return adc_out

# Infinite loop for reading ADC value after 1 sec
while True:
	reading=analog_read(1)
	print reading
	time.sleep(1)
