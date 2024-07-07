from gpiozero import Servo 			# Importing library that controls the servo					# type: ignore 
from time import sleep 			# Importing library for delaying

Correcc: float = 0.50 			# Ammount that I am correcting the defined pulse width of the servo by
maxPW: float = (2.0 + Correcc) / 1000 			# Setting the new max pulse width of the servo
minPW: float = (1.0 - Correcc) / 1000 			# Settng the new minimum pulse width of the servo
servo = Servo(12,min_pulse_width=minPW,max_pulse_width=maxPW) 			# Making a servo object name "servo", on pin 12 with the minimum pulse width of minPW and maximum pulse width of maxPW

def main():
	while True: 			# Runs code repeatedly
		prompt: str = input("Would you like the servo to jump or sweep? ") 			# Asks the user if they want the servo to jump between angles or sweep between them.
		if "jump" in prompt and "sweep" not in prompt: 			# Checks if the user said "jump"
			print("Great! Running jump code..") 			# Prints the text within quotations
			sleep(0.5) 			# Delays half a second
			jump() 			# Runs the Jump function
		elif "sweep" in prompt and "jump" not in prompt: 			# Checks if the user said "sweep"
			print("Great! Running sweep code..") 			# Prints the text within quotations
			sleep(0.5)			# Delays half a second
			sweep() 			# Runs the sweep function
		else: 			# Runs the following code if neither of the above criteria are met
			print("Error! Your input was not valid. Try 'jump' or 'sweep.'") 			# Prints the text within quotations
			sleep(1.5) 			# Delays for 1.5 seconds
			continue 			# Resets the while loop


def jump(): 			# Defining statement for the "jump" function
	while True: 			# Runs code repeatedly
		servo.min() 			# Sets servo to it's minimum angle
		sleep(0.5) 			# Delays for half a second
		servo.mid() 			# Sets servo to it's middle angle
		sleep(0.5) 			# Delays for half a second
		servo.max() 			# Sets servo to it's maximum angle 
		sleep(0.5) 			# Delays for half a second


def sweep(): 			# Defining statement for the "sweep" function
	while True: 			# Runs code repeatedly
		for i in range(0,21): 			# Loops through 21 times, starting with a value of 0 for i and incrementing to 20
			ang = (float(i) - 10) / 10 			# Sets the value of ang to i minus 10, divided by 10
			servo.value = ang 			# Sets servo angle to that of ang
			sleep(0.1) 			# Delays for half a second
		for i in range (20, -1, -1): 			# Loops through 21 times, starting at 20 and counting down to 0.
			ang = (float(i) - 10) / 10 			# Sets the value of ang to i minus 10, divided by 10
			servo.value = ang 			# Sets servo angle to that of ang
			sleep(0.1) 			# Delays for half a second


if __name__ == "__main__": 			# Only runs following code if the program being ran is "Servo_Test.py"
	main() 			# Runs the function "main()"