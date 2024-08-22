# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from time import sleep 			# Imports the sleep module from time, used for delaying the code
import busio 			# Imports the busio module 					# type: ignore
import adafruit_bmp3xx 				# Imports the module responsible for controlling the sensor 					 # type: ignore

# ConstInts
SCL = 2 			# Defines the SCL variable to 2, for where the SCL pin located on the pi.
SDA = 3 			# Defines the SDA variable to 3, for where the SDA pin is located on the pi.
MtrsToFt = 3.281 				# The value one must multiply meters by convert to feet.

# I2C setup
i2c = busio.I2C(SDA, SCL) 			# Defining where SDA and SCL pins are.
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c, address = 0x76) 			# Making a sensor object name "BMP" at I2C address of 0x76

bmp.altitude_oversampling = 4			# Defines oversampling value for altitude
#bmp.pressure_oversampling = 8 			# Defines oversampling value for pressure
#bmp.temperature_oversampling = 2 			# Defines oversampling value for temperature

try: 			#Tries to run the following code, and runs code according to except blocks if not possible
	while True: 			# Runs code repeatedly
		alt = round(bmp.altitude, 3) 			# Takes the read altitude and rounds it to 3 decimal places, assigning that value to the variable alt
		FtAlt = round((alt * MtrsToFt) , 3)
		print("The altitude is " + str(alt) + " meters.") 			# Prints out the altitude in meters
		print("That is " + str(FtAlt) + " feet.") 				# Prints the altitude in feet
		sleep(1) 			#Delays for 1 second
except KeyboardInterrupt: 			# Runs the following code whenever the user stop the program, such as through ctrl - c.
	print("") 			# Prints an empty line so that ^C is not on the same line as the exception.
	print("Program stopepd by user interrupt!") 			# Prints out the text within the quotation marks.