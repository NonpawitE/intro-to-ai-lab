#!/usr/bin/env python3

"""
Week 1 : Exercise 2

Face detection from webcam
"""

import cv2 as cv

# Define webcam
cam         = cv.VideoCapture(0)

# Import cascade and create classifier
cascade     = 'haarcascade_frontalface_default.xml'
classifier  = cv.CascadeClassifier(cascade)

# Loop until 'q' button pressed
while cv.waitKey(1) != 27:
    # Capture an image from webcam
    _, img  = cam.read()

    # Convert image to grayscale
    gray    = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Detect face and extract position
    pos     = classifier.detectMultiScale(gray)

    # Draw square around detected face(s)
    for (x, y, w, h) in pos:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Show output
    cv.imshow("Face Detection", img)

# Close cam
cam.release()
# Close window
cv.destroyAllWindows()