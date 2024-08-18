																								#Currently Untested!!

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from time import sleep 			# Imports the sleep module from time, used for delaying the code
import busio 			# Imports the busio module 					# type: ignore
import adafruit_bmp3xx 				# Imports the module responsible for controlling the sensor 					 # type: ignore

# I2C setup
i2c = busio.I2C(3, 2) 			# Defining i2c addr, uses busio.SCL and busio.SDA
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c, address = 0x76) 			# Making a sensor object name "BMP"

bmp.pressure_oversampling = 8 			# Defines oversampling value for pressure
bmp.temperature_oversampling = 2 			# Defines oversampling value for temperature

while True: 			# Runs code repeatedly
    print(				#Prints out the pressure and temperature
        "Pressure: {:6.4f}  Temperature: {:5.2f}".format(bmp.pressure, bmp.temperature)
    )
    sleep(1) 			#Delays for 1 second
