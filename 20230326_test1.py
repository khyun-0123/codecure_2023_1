import cv2
import numpy as np

# Load the image
image_path = input("Enter the path of the image file: ")
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find the contours of the black lines in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask from the contours
mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.drawContours(mask, contours, -1, (255, 255, 255), 2, cv2.LINE_AA)``

# Invert the mask to create a mask of the background
background_mask = cv2.bitwise_not(mask)

# Apply the mask to the original image to create an image with only the black lines
lines = cv2.bitwise_and(image, image, mask=mask)

# Apply the background mask to the original image to create an image with the background
background = cv2.bitwise_and(image, image, mask=background_mask)

# Show the images with the black lines and background separately
cv2.imshow("Lines", lines)
cv2.imshow("Background", background)
cv2.waitKey(0)

# Crop the image along the black lines
x, y, w, h = cv2.boundingRect(mask)
cropped = image[y:y+h, x:x+w]

# Show the cropped image
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()