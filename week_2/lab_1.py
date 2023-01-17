#!/usr/bin/env python3

"""
Week 1 : Exercise 1

Face detection from image
"""

import cv2 as cv

# Import image
img         = cv.imread('test_face.jpg')

# Import cascade and create classifier
cascade     = 'haarcascade_frontalface_default.xml'
classifier  = cv.CascadeClassifier(cascade)

# Convert image to grayscale
gray        = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect face and extract position
pos         = classifier.detectMultiScale(gray)

# Draw square around detected face(s)
for (x, y, w, h) in pos:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
# Show output
cv.imshow("Face Detection", img)

# Wait for any key to be pressed
cv.waitKey(0)
# Close window
cv.destroyAllWindows()