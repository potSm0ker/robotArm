import numpy as np
import cv2
#this script detects all objects in camera view and displays coordinates and bounding box
#use trackbars to adjust amount of objects detected

def nothing(x):
    pass


cv2.namedWindow("Trackbar")
cv2.createTrackbar("Threshold1", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Threshold2", "Trackbar", 0, 255, nothing)

# Set window size
window_width = 800
window_height = 600

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_original = frame.copy()

    thresh1 = cv2.getTrackbarPos("Threshold1", "Trackbar")
    thresh2 = cv2.getTrackbarPos("Threshold2", "Trackbar")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    edged = cv2.Canny(blurred, thresh1, thresh2, 3)
    dilated = cv2.dilate(edged, (1, 1), iterations=2)

    contours, hierarchy = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        # Calculate the coordinates and dimensions of the bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)

        # Draw a bounding box around the object
        cv2.rectangle(img_original, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the coordinates on the frame
        text = f'({x}, {y})'
        cv2.putText(img_original, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Resize window
    cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Output", window_width, window_height)

    cv2.imshow("Output", img_original)

    if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
