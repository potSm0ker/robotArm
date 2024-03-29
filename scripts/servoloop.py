import time
from adafruit_servokit import ServoKit
#this script was generated by chatgpt 3.5 august 3 2023 version
# Initialize the Servo HAT
kit = ServoKit(channels=16)  # Change the number of channels as needed

# Define the servo channel you want to control
servo_channel = 0  # Replace with the channel your servo is connected to


#fast speed and wide open angle. scissors needs to open wide enough to give buds time to get to middle of blade opening. There is more torque towards the middle of the blades. 
# buds and stems may get stuck on scissors
#servo needs higher voltage
# the tip of the scissors do not have enough torque to cut through branches/ cut buds of branches
# resin buildup on the tip of the scissors quickly reduces cutting motion the scissors will stick together and fail to open


# Define servo angle limits (adjust as needed)
min_angle = 71  # Minimum servo angle
max_angle = 178  # Maximum servo angle

# Define servo speed and direction (adjust as needed)
# speed 3 max, bud needs time to travel into cutting range(middle of scissors)


servo_speed = 3  # Speed of servo movement (larger values are faster)
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
