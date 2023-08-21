import cv2
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras_frcnn import FasterRCNN
from keras_frcnn.utils import simple_parser, get_new_img_size

# Load the trained model
model = FasterRCNN()

# Load the input image
img = cv2.imread('brightness down.png')

# Detect objects in the image
boxes, labels, scores = model.predict(img)

# Extract objects from the table
for i, box in enumerate(boxes):
    x1, y1, x2, y2 = box
    object_img = img[y1:y2, x1:x2]
    cv2.imwrite('object_{}.jpg'.format(i), object_img)