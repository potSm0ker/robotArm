#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device

# this will open and close the scissors attached to the claw, this script opens and closes the 6th servo

Arm = Arm_Device()
time.sleep(.1)

time_1 = 500
time_2 = 1000
time_sleep = 0.1

# controls individual servos 

def main():
    #controls all servos at once (1,2,3,4,5,6,time to complete)
    Arm.Arm_serial_servo_write6(90, 75, 45, 75, 90, 120, 500)
    time.sleep(.1)
    count = 0

    while True:
        #three values for servo control (servo number, angle, time to complete)
        Arm.Arm_serial_servo_write(4, 75, 1)
        time.sleep(1.5)
        print("open")
        Arm.Arm_serial_servo_write(6, 25, time_1)
        time.sleep(1.5)
        print("close")
        Arm.Arm_serial_servo_write(6, 120, time_1)
        time.sleep(1.5)
        
        count += 1
        print(f"Trim! {count}")


try :
    main()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass

del Arm 
