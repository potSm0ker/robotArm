#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device

#resets arm to middle position

# look_at_tray = [90, 135, 0, 0, 90, 30]

Arm = Arm_Device()
time.sleep(.1)

def main():
    dir_state = 1
    look_at = [90, 164, 18, 0, 90, 90]

    Arm.Arm_serial_servo_write6(90, 165, 0, 0, look_at[5], 60, 500)
    time.sleep(1)
    
    while True:
        if dir_state == 1:
            Arm.Arm_serial_servo_write6(90, 165, 0, 0, 90, 90, 500)
            time.sleep(1)
        else:
            print("u fucked up")
            time.sleep(1)



try :
    main()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass


del Arm  

