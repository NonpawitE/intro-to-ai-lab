#!/usr/bin/env python3

"""
Example 1 : Mask or Unmasked Detection

Output : https://youtu.be/JiC2getn-gE
"""

import cv2 as cv
from keras.models import load_model
import numpy as np

# Define webcam
cam             = cv.VideoCapture(0)

# Import cascade and create classifier
cascade         = 'haarcascade_frontalface_default.xml'
classifier      = cv.CascadeClassifier(cascade)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model           = load_model('keras_Model.h5', compile=False)

# Load the labels
labels          = open('labels.txt', 'r').readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data            = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Loop until 'esc' button pressed
while cv.waitKey(1) != 27:
    _, img      = cam.read()
    rgb_img     = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    gray        = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    pos = classifier.detectMultiScale(gray)
    for(x,y,w,h) in pos:
        face    = rgb_img[y:y+h,x:x+w]
    
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        image   = cv.resize(face, (224, 224), interpolation=cv.INTER_AREA)
        
        # Make the image a numpy array and reshape it to the models input shape.
        image   = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        # Normalize the image array
        image    = (image / 127.5) - 1
         
        # Have the model predict what the current image is. Model.predict
        # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
        # it is the first label and 80% sure its the second label.
        prediction = model.predict(image, verbose = 0)
        index = np.argmax(prediction)
        class_name = labels[index]
        confidence_score = prediction[0][index]
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    print('Class:', class_name, end='')
    print('Confidence score:', confidence_score)
    
    # Show output
    cv.imshow("Face Detection", img)

# Close cam
cam.release()
# Close window
cv.destroyAllWindows()