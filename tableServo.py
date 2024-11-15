import pigpio
import time

servo = 18


pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency(servo, 50)

pwm.hardware_PWM(servo, 50, 30000)
time.sleep(5)

pwm.hardware_PWM(servo, 50, 30589)
time.sleep(5)

pwm.hardware_PWM(servo, 50, 30882)
time.sleep(5)

pwm.hardware_PWM(servo, 50, 31176)
time.sleep(5)

pwm.hardware_PWM(servo, 50, 31470)
time.sleep(5)

pwm.hardware_PWM(servo, 50, 31764)
time.sleep(5)
