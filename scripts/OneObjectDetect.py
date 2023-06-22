import cv2
import numpy as np


def detect_object(image, template):
    # Convert images to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Get the top-left corner coordinates of the matched region
    top_left = max_loc

    # Get the dimensions of the template
    height, width = template.shape[:2]

    # Calculate the bottom-right corner coordinates of the matched region
    bottom_right = (top_left[0] + width, top_left[1] + height)

    # Draw a rectangle around the matched region
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    # Display the coordinates on the frame
    text = f'({top_left[0]}, {top_left[1]})'
    cv2.putText(image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return image


# Load the template image
template_image = cv2.imread("template.png")

# Set window size
window_width = 800
window_height = 600

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect the object and display its coordinates
    output = detect_object(frame, template_image)

    # Resize window
    cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Output", window_width, window_height)

    cv2.imshow("Output", output)

    if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
