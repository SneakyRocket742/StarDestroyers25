from gpiozero import Servo
from time import sleep

Correc = 0.50
maxPW = (2.0 + Correc) / 1000
minPW = (1.0 - Correc) / 1000
servo = Servo(12,min_pulse_width=minPW,max_pulse_width=maxPW)

while True:
#	servo.min()
#	sleep(0.5)
#	servo.mid()
#	sleep(0.5)
#	servo.max()
#	sleep(0.5) 
	servo.min()
	sleep(1)
	servo.max()
	sleep(1)
