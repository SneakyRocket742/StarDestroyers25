import time 			# Allows delaying
from DFRobot_BMX160 import BMX160 			# Library used to control accelerometer 							# type: ignore

ctrl = 1 			# Defining the location of the control pin
alf = BMX160(ctrl) 			# Creating and defining the sensor object as 'alf'


while not alf.begin(): 			# Attempts to begin, returns True if succeed, otherwise returns False
	time.sleep(2) 			# Delays for 2 seconds

def AccelGet():
    data = alf.get_accel()
    accel = sqrt((data[6] * data[6]) + (data[7] * data[7]) + (data[8] * data[8]))
    return accel

def main(): 			# Main function where most of the code is ran
	while True: 			# Loops the following code forever; First gets all data and assings it to the 'data' variable, and then waits 1 second and prints it out before repeating
		data= alf.get_all_data() 			# Appends all data from the sensor onto the 'data' variable
		time.sleep(1) 			# Delay's for one second
        a = AccelGet()
		print("accel magnitude: {0:.2f} m/s^2.".format(a) 			# Print's out all of the acceleromter readings, being formated by the 'format' utility
