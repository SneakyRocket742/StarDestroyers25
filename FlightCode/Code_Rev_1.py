from gpiozero import Servo          # This module is used to control the servo
from DFRobot_BMX160 import BMX160 			# This module is used to control the Accelerometer
from time import sleep              # This module is used to implement delays in the code.
from statistics import mean             # This module is used to help average out and smooth out the data, smoothing out floating point errors.
from math import sqrt
import sys          # This module is used to help manipulate the interpretor
import busio 			# This module is used to implement I2C capabilities for communicating with the sensors.
import adafruit_bmp3xx 			# This module is used to control the altimeter.
import array
import os

##Variables##
AccelCtrl = 1           # Defines the location of the control pin for the Accelerometer.
SCL = 2 			# Defines the SCL variable to 2, for where the SCL pin located on the pi.
SDA = 3 			# Defines the SDA variable to 3, for where the SDA pin is located on the pi.
MtrsToFt = 3.281 			# The value one must multiply meters by convert to feet.
TargetAlt = 750
Correcc: float = 0.50 			# Amount that I am correcting the defined pulse width of the servo by
maxPW: float = (2.0 + Correcc) / 1000 			# Setting the new max pulse width of the servo
minPW: float = (1.0 - Correcc) / 1000 			# Setting the new minimum pulse width of the servo
ArmDly = 10
AccelChcks = 3
accelTrgr = 11  # CHANGE BACK TO 18 BEFORE LAUNCH!!!!!!
dumpSize = 10
sleep_delay = 0.005
shutdownTime = 10
GrndAlt = 0

##Setup##
def setup():
	global servo
	global alf
	global bmp
	sys.path.append('../../')
	servo = Servo(12, min_pulse_width=minPW, max_pulse_width=maxPW) 			# Making a servo object name "servo", on pin 12 with the minimum pulse width of minPW and maximum pulse width of maxPW
	alf = BMX160(AccelCtrl) 			# Creating and defining the sensor object as 'alf'
	i2c = busio.I2C(SDA, SCL) 			# Defining where SDA and SCL pins are.
	bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c, address = 0x76) 			# Making a sensor object name "BMP" at I2C address of 0x76
	bmp.altitude_oversampling = 4			# Defines oversampling value for altitude

##Ground Testing##
def grndTest():
    print("Testing and calibrating altitude")
    global GrndAlt
    GrndAlt = AltGet(3)
    print(f"The relative altitude is {GrndAlt - AltGet(1)}, while the actual altitude is {AltGet(1)}")
    sleep(0.5)
    print("Starting Accel Checks.")
    print(f"If {accelTrgr} is not equal to 18, NO GO! Change the value in the code.")
    for i in range(AccelChcks):
        Accel = AccelGet()
        print(f"The relative acceleration is {Accel}")
        sleep(0.5)
    print("Starting Airbreak Sweep in t-5. Stand Clear!")
    sleep(5)
    AirBrkSwp(3)
    print("Airbreak Sweep complete! Moving to standby")

##Launch Loop##
def launch():
    print("Standby for launch")
    maxAccel = 0
    while True:
        accel = AccelGet()
        if accel > maxAccel:
            maxAccel = accel
        if accel >= accelTrgr:
            print("Launch detected!")
            break
    runtime = 0
    alts = array.array('d')             # d is floating point data
    file = open('/home/tarc/2025-Code/FlightData/Test0', 'w')
    Triggered = False
    while True:
        CurAlt = AltGet(1) - GrndAlt
        alts.append(CurAlt)
        dataLength = alts.buffer_info()[1]
        if dataLength >= dumpSize:
            break
        alts.append(CurAlt)
        dataLength = alts.buffer_info()[1]
        if dataLength >= dumpSize:
            for alt in alts:
                file.write(f"{alt}\n")
            alts = array.array('d')
        sleep(sleep_delay)
        runtime += sleep_delay

        for alt in alts:
            file.write(f"{alt}\n")
        alts = array.array('d')
        sleep(sleep_delay)
        runtime += sleep_delay

        if CurAlt >= TargetAlt:
            print("Deploying Airbrakes!")
            for alt in alts:
                file.write(f"{alt}\n")
            servo.max()
            alts = array.array('d')
            break
    while True:
        CurAlt = AltGet(1) - GrndAlt
        alts.append(CurAlt)
        dataLength = alts.buffer_info()[1]
        if dataLength >= dumpSize:
            break
        alts.append(CurAlt)
        dataLength = alts.buffer_info()[1]
        if dataLength >= dumpSize:
            for alt in alts:
                file.write(f"{alt}\n")
            alts = array.array('d')
        sleep(sleep_delay)
        runtime += sleep_delay

        for alt in alts:
            file.write(f"{alt}\n")
        alts = array.array('d')
        sleep(sleep_delay)
        runtime += sleep_delay
        if runtime >= shutdownTime:
            file.close()
            return

 #Altitude Acquisition#
def AltGet(Repetitions):
    alt = 0
    for i in range(Repetitions):
        alt += bmp.altitude
    alt /= Repetitions    
    alt = round(alt * MtrsToFt, 3)
    return(alt)

#Acceleration Acquisition#
def AccelGet(): 
    data = alf.get_all_data()
    accel = sqrt((data[6] * data[6]) + (data[7] * data[7]) + (data[8] * data[8]))
    return accel

#Airbreak Sweep#
def AirBrkSwp(Repetitions):
    servo.min()
    for i in range(Repetitions):
        servo.max()
        sleep(1)
        servo.min()
        print(f"Airbrake iteration {i + 1} complete!")
        sleep(1.5)


def main():
    setup()
    grndTest()
    launch()

if __name__ == '__main__':
    main()
