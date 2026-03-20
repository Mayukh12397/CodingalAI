import cv2
import numpy as np


# Set up webcam capture
cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()


    if not ret:
        print("Error: Failed to capture image.")
        break




    # Convert to HSV for color filtering
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # Define the range for skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)


    # Create a mask to detect skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)


    # Apply the mask to the frame
    result = cv2.bitwise_and(frame, frame, mask=mask)


    # Find contours (hand shape) in the masked image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # If contours are found, draw them
    if contours:
        max_contour = max(contours, key=cv2.contourArea)  # Get largest contour
        if cv2.contourArea(max_contour) > 500:  # Ignore small contours
            # Draw the bounding box around the detected hand
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


            # Get the center of the hand for further tracking or interaction
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)  # Red dot at center


    # Display the original and result frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Filtered Frame', result)


    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

# WHAT IS HSV?
# An HSV color filter is a way to select or change colors in an image based on how humans naturally describe color.
# Instead of using the usual RGB (Red, Green, Blue), it uses HSV, which stands for:
# Hue (H) → the type of color (red, blue, green, etc.)
# Saturation (S) → how strong or dull the color is.
# Value (V) → how bright or dark the color is.

# WHAT IS CONTOUR?
# A contour is just the outline (boundary) of an object in an image.
# It can be understood like:
# Drawing a line around an object
# Like tracing the edges of a shape.


