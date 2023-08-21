import cv2
import numpy as np

img1 = cv2.imread('C:/Users/jhkim/OneDrive/바탕 화면/CodeCure/sangmyung restaurat.png')
cv2.imshow('image1',img1)

#img1 = cv2.imread('C:/Users/jhkim/OneDrive/바탕 화면/CodeCure/sangmyung restaurat.png', cv2.IMREAD_GRAYSCALE)

#cm2.imwrite('grayrestaurant.jpg, img1, [cv2.IMWRITE_PNG_QUALITY,100]')

cv2.waitkey(0)
cv2.destroyALlwindows()
