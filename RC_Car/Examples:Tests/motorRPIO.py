"""
Motor Program for RC car Drone
Working!
"""

from RPIO import PWM
import time


motor = PWM.Servo()
pin1 = 18 //This sets the pin used to control your motor
delay_period = 10 //delay time, in seconds. 

motor.set_servo(pin1, 600) #sets motor on to 600uS - full speed (8V)
time.sleep(delay_period)

motor.set_servo(pin1, 1800) #sets motor on to 1800uS - Reverse? full speed (-8V)
time.sleep(delay_period)

motor.set_servo(pin1, 0) #sets motor to neutral- 0V?
time.sleep(2*delay_period)

motor.stop_servo(pin1)