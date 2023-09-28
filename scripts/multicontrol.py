import time
from adafruit_servokit import ServoKit
import cv2
import numpy as np

# Initialize the Servo HAT
kit = ServoKit(channels=16)  # Change the number of channels as needed

# Define the servo channels you want to control
servo_channels = [0, 1]  # Replace with the channels your servos are connected to

# Define servo angle limits (adjust as needed)
min_angle = 65  # Minimum servo angle
max_angle = 130  # Maximum servo angle

# Create a function to update the servo angles based on the slider values
def update_servo_angles(slider_values):
    for i, channel in enumerate(servo_channels):
        angle = int(slider_values[i])
        kit.servo[channel].angle = angle

# Create a window with sliders to control the servo angles
cv2.namedWindow("Servo Control")
initial_slider_values = [min_angle] * len(servo_channels)
cv2.createTrackbar("Servo 1 Angle", "Servo Control", min_angle, max_angle, update_servo_angles)
cv2.createTrackbar("Servo 2 Angle", "Servo Control", min_angle, max_angle, update_servo_angles)
cv2.createTrackbar("Servo 3 Angle", "Servo Control", min_angle, max_angle, update_servo_angles)
cv2.createTrackbar("Servo 4 Angle", "Servo Control", min_angle, max_angle, update_servo_angles)
cv2.createTrackbar("Servo 5 Angle", "Servo Control", min_angle, max_angle, update_servo_angles)

try:
    while True:
        # Read the current slider values (angles)
        current_angles = [cv2.getTrackbarPos(f"Servo {i + 1} Angle", "Servo Control") for i in range(len(servo_channels))]

        # Create a black frame to display the servo angle text
        frame = np.zeros((100, 400, 3), dtype=np.uint8)

        # Display the servo angles on the OpenCV window
        angle_text = ", ".join([f"Servo {i + 1}: {angle}" for i, angle in enumerate(current_angles)])
        cv2.putText(frame, angle_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the frame with angle information
        cv2.imshow("Servo Control", frame)

        # Check for key presses (ESC to exit)
        key = cv2.waitKey(10)
        if key == 27:  # ESC key
            break

except KeyboardInterrupt:
    # Stop the servos and exit gracefully when Ctrl+C is pressed
    for channel in servo_channels:
        kit.servo[channel].angle = None

# Release OpenCV window and cleanup
cv2.destroyAllWindows()
