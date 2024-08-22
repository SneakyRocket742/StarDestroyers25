####################################<Credits>####################################

'''!
  @file read_all_data.py
  @brief Through the example, you can get the sensor data by using getSensorData:
  @n     get all data of magnetometer, gyroscope, accelerometer.
  @n     With the rotation of the sensor, data changes are visible.
  @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author [luoyufeng] (yufeng.luo@dfrobot.com)
  @maintainer [Fary](feng.yang@dfrobot.com)
  @version  V1.0
  @date  2021-10-20
  @url https://github.com/DFRobot/DFRobot_BMX160
'''
###################################</Credits>####################################



import sys 			# Module used to manipulate the interpreter
sys.path.append('../../') 			# Configuring path of sys
import time 			# Allows delaying
from DFRobot_BMX160 import BMX160 			# Library used to control accelerometer 							# type: ignore

ctrl = 1 			# Defining the location of the control pin
alf = BMX160(ctrl) 			# Creating and defining the sensor object as 'alf'


while not alf.begin(): 			# Attempts to begin, returns True if succeed, otherwise returns False
	time.sleep(2) 			# Delays for 2 seconds

def main(): 			# Main function where most of the code is ran
	while True: 			# Loops the following code forever; First gets all data and assings it to the 'data' variable, and then waits 1 second and prints it out before repeating
		data= alf.get_all_data() 			# Appends all data from the sensor onto the 'data' variable
		time.sleep(1) 			# Delay's for one second

# 		 	Prints out each of the data. We only want accelerometer data, so all the others are commented.
#        print("magn: x: {0:.2f} uT, y: {1:.2f} uT, z: {2:.2f} uT".format(data[0],data[1],data[2]))
#        print("gyro  x: {0:.2f} g, y: {1:.2f} g, z: {2:.2f} g".format(data[3],data[4],data[5]))
#        print(" ")

		print("accel x: {0:.2f} m/s^2, y: {1:.2f} m/s^2, z: {2:.2f} m/s^2".format(data[6],data[7],data[8])) 			# Print's out all of the acceleromter readings, being formated by the 'format' utility
		print(" ") 			#Prints an empty line to allow for better readability.

if __name__ == "__main__": 				# Only runs the 'main' function if the program is not being executed by and outside program. I.E, this won't be ran if this code is imported as a module into another program
	try: 			# Tries to run the following code, and runs the code within the 'except' or 'finally' blocks if unable to
		main() 			# Run's the 'main()' function
	except KeyboardInterrupt: 			# Runs the following code if a keyboard interrupt occurs
		print(" ") 				# Prints an empty line for readabilities sake
		print("Program stopped by user.") 			# Prints the text within the quotation marks to explain what happened
		