import cv2
import numpy as np

# 이미지를 불러온다.
img = cv2.imread('sangmyung restaurat.png')

# 이미지를 HSV 색상 공간으로 변환한다.
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 밝기 채널 (V)을 추출한다.
v_channel = hsv[:, :, 2]

# 밝기 채널에서 가장 높은 값을 갖는 픽셀을 찾는다.
max_value = np.max(v_channel)
max_loc = np.where(v_channel == max_value)

# 해당 픽셀의 위치를 기반으로 원래 이미지에서 진한 부분을 잘라낸다.
x = max_loc[1][0]
y = max_loc[0][0]
h = 100  # 잘라낼 영역의 높이
w = 100  # 잘라낼 영역의 너비
dark_part = img[y:y+h, x:x+w]

# 결과 이미지를 출력한다.
cv2.imshow('Dark part', dark_part)
cv2.waitKey(0)
cv2.destroyAllWindows()
