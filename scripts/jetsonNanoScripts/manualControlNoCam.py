import tkinter as tk
import time
from Arm_Lib import Arm_Device

#generated by free chatGPT may 24th version

#use to control yahboom 6dof robot arm using sliders, numbers correspond to angle of servo motors 1 thru 6

# Initialize the servo control device
Arm = Arm_Device()
time.sleep(.1)

# Define the servo angles
#arm will point straight in air with all  servos set to 90 degree angle
servo_angles = [90, 90, 90, 90, 90, 90]

# Define the slider callback function
def update_servo_angle(event, index):
    servo_angle = sliders[index].get()
    servo_angles[index] = servo_angle
    # 6 sliders control each individual servo  (number of servo to control, servo angle 0 to 180, time to completion of angle)
    Arm.Arm_serial_servo_write(index + 1, servo_angle, 200)

# Create the main Tkinter window
window = tk.Tk()
window.title("Servo Control")

# Create the sliders
sliders = []
for i in range(6):
    slider = tk.Scale(window, from_=0, to=180, resolution=1, orient=tk.HORIZONTAL, label=f"Servo {i+1}", length=300)
    slider.set(servo_angles[i])
    slider.bind("<ButtonRelease-1>", lambda event, index=i: update_servo_angle(event, index))
    slider.pack()
    sliders.append(slider)

# Main Tkinter event loop
window.mainloop()

def main():
    try:
        window.mainloop()
    except KeyboardInterrupt:
        print("I'll be back")
        pass

if __name__ == "__main__"
    main()

# Cleanup
del Arm
