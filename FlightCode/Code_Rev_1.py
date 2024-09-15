from gpiozero import Servo 			# type: ignore
from DFRobot_BMX160 import BMX160 			# type: ignore
from time import sleep
from statistics import mean
import sys
import busio 			# type: ignore
import adafruit_bmp3xx 			# type: ignore

##variables##
AccelCtrl = 1
SCL = 2 			# Defines the SCL variable to 2, for where the SCL pin located on the pi.
SDA = 3 			# Defines the SDA variable to 3, for where the SDA pin is located on the pi.
MtrsToFt = 3.281 			# The value one must multiply meters by convert to feet.
TargetAlt = 750
Correcc: float = 0.50 			#Ammount that I am correcting the defined pulse width of the servo by
maxPW: float = (2.0 + Correcc) / 1000 			#Setting the new max pulse width of the servo
minPW: float = (1.0 - Correcc) / 1000 			#Setting the new minimum pulse width of the servo
ArmDly = 10

##Setup##
def setup():
	sys.path.append('../../')
	servo = Servo(12,min_pulse_width=minPW,max_pulse_width=maxPW) 			#Making a servo object name "servo", on pin 12 with the minimum pulse width of minPW and maximum pulse width of maxPW
	alf = BMX160(AccelCtrl) 			# Creating and defining the sensor object as 'alf'
	i2c = busio.I2C(SDA, SCL) 			# Defining where SDA and SCL pins are.
	bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c, address = 0x76) 			# Making a sensor object name "BMP" at I2C address of 0x76
	bmp.altitude_oversampling = 4			# Defines oversampling value for altitude

##Ground Testing##
def grndTest():
    print("Testing and calibrating altitude")
    GrndAlt = round(mean(AltGet(3)))
    CalAlt = AltGet(1) - GrndAlt
    print(f"The relative altitude is {CalAlt}, while the actual altitude is {AltGet(1)}")
    sleep(0.5)
    print("Starting Accel Checks.")
    for i in range(AccelChcks):
        Accel = AccelGet(1)
        print(f"The acceleration is as follows. x: {alt[6]} m/s^2, y: {alt[7]} m/s^2, z:{alt[8]} m/s^2")
        sleep(0.5)
    print("Starting Airbreak Sweep in t-5. Stand Clear!")
    sleep(5)
    AirBrkSwp(3)
    print("Airbreak Sweep complete! Moving to standby")

##Standby##
def standby():
    print(f"Warning! Arming in t-{ArmDly} seconds!")
    delay(ArmDly)
    print("In standby! Avoid sudden movements")
    Launch = False
    while not Launch:
        Accel = AccelGet(1)
        if Accel[7] >= -18:
            print("Launch detected!")
            Launch = True
##Flight##
def flight():
    print("liftoff!")
    triggered = False
    while not triggered:
        FlightAlt = AltGet(1) - CalAlt
        AccelGet(1)
        print(f"The altitude is {FlightAlt}, and the acceleration data is as follows. X:{alt[6]} m/s^2, Y:{alt[7]} m/s^2, Z:{alt[8]} m/s^2")
        if AltGet(1) >= TargetAlt:
            strikes = strikes + 1
            if strikes >= 3:
                triggered = True
        else:
            strikes = 0

##Deployment##
def deploy():
    print("Deploying Airbrakes!")
    servo.max()
    print("Deployed")
    flying = True
    strikes = 0
    while flying:
        FlightAlt = AltGet(1) - CalAlt
        AccelGet(1)
        print(f"The altitude is {FlightAlt}, and the acceleration data is as follows. X:{alt[6]} m/s^2, Y:{alt[7]} m/s^2, Z:{alt[8]} m/s^2")
        if AltGet(1) <= 0:
            strikes = strikes + 1
            if strikes >= 3:
                print("Warning! Shutdown in t-30 secconds")
                sleep(30)
                flying = False
    else:
        strikes = 0


#Altitude Acquisition#
def AltGet(Repetitions):
    alt = 0
    for i in range(Repetitions):
        alt = bmp.altitude
        alt = round(alt * MtrsToFT, 3)
    alt = mean(alt)
    return(alt)
#Acceleration Acquisition#
def AccelGet():
    accel = round(alf.get_accel(), 3)

#Airbreak Sweep#
def AirBrkSwp(Repetitions):
    for i in range(Repeititions):
        for n in range(0,21):
            ang = (float(i) - 10) / 10
            servo.value = ang
            sleep(0.1)
        for n in range(20, -1, -1):
            ang = (float(i) - 10) / 10
            servo.value = ang
            sleep(0.1)
        print(f"Sweep iteration {i + 1} complete!")
            delay(1.5)


def main():
    setup()
    grndtest()
    standby()
    flight()
    deploy()

if __name__ == '__main__':
    main()
