import time
from adafruit_servokit import ServoKit

# Initialize the Servo HAT
kit = ServoKit(channels=16)  # Change the number of channels as needed

# Define the servo channel you want to control
servo_channel = 0  # Replace with the channel your servo is connected to

# Define servo angle limits (adjust as needed)
min_angle = 0  # Minimum servo angle
max_angle = 180  # Maximum servo angle

# Define servo speed and direction (adjust as needed)
servo_speed = 1  # Speed of servo movement (larger values are faster)
direction = 1    # 1 for clockwise, -1 for counterclockwise

try:
    while True:
        # Move the servo from min to max angle
        for angle in range(min_angle, max_angle + 1, servo_speed * direction):
            kit.servo[servo_channel].angle = angle
            time.sleep(0.01)  # Adjust delay for smoother motion

        # Move the servo from max to min angle
        for angle in range(max_angle, min_angle - 1, -servo_speed * direction):
            kit.servo[servo_channel].angle = angle
            time.sleep(0.01)  # Adjust delay for smoother motion

except KeyboardInterrupt:
    # Stop the servo and exit gracefully when Ctrl+C is pressed
    kit.servo[servo_channel].angle = None
