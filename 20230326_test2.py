import cv2

# Load image
image_path = "D:/test2/sangmyung_restaurat.png"
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to segment the image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 10)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over contours
for i, contour in enumerate(contours):
    # Find the minimum area rectangle that bounds the contour
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = box.astype(int)

    # Crop the image using the bounding box and save as separate image file
    x, y, w, h = cv2.boundingRect(contour)
    roi = image[y:y+h, x:x+w]
    cv2.imwrite(f"ROI_{i}.jpg", roi)