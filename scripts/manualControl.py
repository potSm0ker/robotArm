import tkinter as tk
import time
from Arm_Lib import Arm_Device

# Initialize the servo control device
Arm = Arm_Device()
time.sleep(.1)

# Define the servo angles
servo_angles = [90, 90, 90, 90, 90, 90]

# Define the slider callback function
def update_servo_angle(event, index):
    servo_angle = sliders[index].get()
    servo_angles[index] = servo_angle
    Arm.Arm_serial_servo_write(index + 1, servo_angle, 10)

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

# Cleanup
del Arm
