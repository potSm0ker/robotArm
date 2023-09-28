import time
from adafruit_servokit import ServoKit
import cv2
import numpy as np

# Initialize the Servo HAT
kit = ServoKit(channels=16)  # Change the number of channels as needed

# Define the servo channel you want to control
servo_channel = 0  # Replace with the channel your servo is connected to

# Define servo angle limits 65-130 to avoid damage to end effector (adjust as needed)
min_angle = 0  # Minimum servo angle
max_angle = 180  # Maximum servo angle

# Create a function to update the servo angle based on the slider value
def update_servo_angle(slider_value):
    angle = int(slider_value)
    kit.servo[servo_channel].angle = angle

# Create a window with a slider to control the servo angle
cv2.namedWindow("Servo Control")
cv2.createTrackbar("Angle", "Servo Control", min_angle, max_angle, update_servo_angle)

try:
    while True:
        # Read the current slider value (angle)
        current_angle = cv2.getTrackbarPos("Angle", "Servo Control")
        #create a black frame to display the servo angle text
        frame = np.zeros((100, 400, 3), dtype=np.uint8)


        # Display the servo angle on the OpenCV window
        cv2.putText(
            frame, f"Servo Angle: {current_angle}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
        )

        #show the frame with angle information
        #cv2.imshow("Servo Control", frame)

        # Check for key presses (ESC to exit)
        key = cv2.waitKey(10)
        if key == 27:  # ESC key
            break

except KeyboardInterrupt:
    # Stop the servo and exit gracefully when Ctrl+C is pressed
    kit.servo[servo_channel].angle = None

# Release OpenCV window and cleanup
cv2.destroyAllWindows()
