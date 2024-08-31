from gpiozero import Servo 			# type: ignore
from DFRobot_BMX160 import BMX160 			# type: ignore
from time import sleep
import sys
import busio 			# type: ignore
import adafruit_bmp3xx 			# type: ignore

##variables##
AccelCtrl = 1
SCL = 2 			# Defines the SCL variable to 2, for where the SCL pin located on the pi.
SDA = 3 			# Defines the SDA variable to 3, for where the SDA pin is located on the pi.
MtrsToFt = 3.281 			# The value one must multiply meters by convert to feet.
Correcc: float = 0.50 			#Ammount that I am correcting the defined pulse width of the servo by
maxPW: float = (2.0 + Correcc) / 1000 			#Setting the new max pulse width of the servo
minPW: float = (1.0 - Correcc) / 1000 			#Settng the new minimum pulse width of the servo

def setup():
	sys.path.append('../../')
	servo = Servo(12,min_pulse_width=minPW,max_pulse_width=maxPW) 			#Making a servo object name "servo", on pin 12 with the minimum pulse width of minPW and maximum pulse width of maxPW
	alf = BMX160(AccelCtrl) 			# Creating and defining the sensor object as 'alf'
	i2c = busio.I2C(SDA, SCL) 			# Defining where SDA and SCL pins are.
	bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c, address = 0x76) 			# Making a sensor object name "BMP" at I2C address of 0x76
	bmp.altitude_oversampling = 4			# Defines oversampling value for altitude

def grndTest():
	pass