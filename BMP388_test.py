# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time 			# Imports the sleep module from time, used for delaying the code
import board 			# Imports the board module
import adafruit_bmp3xx 				# Imports the module responsible for controlling the sensor

# I2C setup
i2c = board.I2C() 			# Defining i2c addr, uses board.SCL and board.SDA
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c) 			# Making a sensor object name "BMP"

bmp.pressure_oversampling = 8 			# Defines oversampling value for pressure
bmp.temperature_oversampling = 2 			# Defines oversampling value for temperature

while True: 			# Runs code repeatedly
    print(				#Prints out the pressure and temperature
        "Pressure: {:6.4f}  Temperature: {:5.2f}".format(bmp.pressure, bmp.temperature)
    )
    time.sleep(1) 			#Delays for 1 second
