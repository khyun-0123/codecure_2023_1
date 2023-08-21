import cv2
import numpy as np

# 이미지 로드
img = cv2.imread('sangmyung restaurat.png')

# 그레이 스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이진화 (임계값 기반 분할)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# 모든 윤곽 찾기
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 윤곽별로 평균 색상 계산
colors = []
for c in contours:
    mask = np.zeros_like(img)
    cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    mean_color = cv2.mean(img, mask=mask)[:3]
    colors.append(mean_color)

# 윤곽선 그리기 및 자르기
for i, c in enumerate(contours):
    mask = np.zeros_like(img)
    cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)
    x, y, w, h = cv2.boundingRect(c)
    roi = img[y:y+h, x:x+w]
    cv2.imwrite(f'region_{i}.png', roi)
