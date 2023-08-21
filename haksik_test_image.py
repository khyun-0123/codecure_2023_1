import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import os
import urllib.request
from PIL import Image
import pytesseract
import cv2
from pytesseract import Output
import pandas as pd
from PIL import Image, ImageEnhance
import datetime
import numpy as np
from collections import deque
import chromedriver_autoinstaller

holiday_num = 0
day_plus = 0
holiday_List = []
discode_print = ""
image_queue = deque()

now = datetime.datetime.now()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome("C:/Program Files/chromedriver.exe")

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.get("https://www.smu.ac.kr/ko/life/restaurantView3.do")
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, "#ko > div.board-name-thumb.board-wrap > ul > li:nth-child(1) > dl > dt > a").click() # 이번주 들어가는 것만
time.sleep(0.5)


# 새로 열린 페이지로 전환 
driver.switch_to.window(driver.window_handles[-1])

# 현재 url 가져오기
final_url = driver.current_url
driver.quit()
print(final_url)
#------------------------------------------------------------------------------현재 url// 이전에는 웹페이지 접속경로임

response = requests.get(final_url)
soup = BeautifulSoup(response.text, "html.parser")

image_tag = soup.select_one(".fr-view img")
image_src = image_tag.get("src")
img_url = "https://www.smu.ac.kr" + image_src

savelocation = now.strftime("%m-%d_%H-%M") + ".png"  # 파일 확장자는 이미지 파일의 확장자로 바꿔주세요.

urllib.request.urlretrieve(img_url, savelocation) #해당 url에서 이미지를 다운로드 메소드
# OCR 기법 사용
img = Image.open(savelocation)
image_path = savelocation
#---------------------------------------------------
#img = img.convert('L') # 이미지 파일을 열어서 grayscale로 변환합니다.

# img.save(savelocation)

img = cv2.imread(savelocation)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection
edged = cv2.Canny(gray, 30, 200) #Canny Edge Detection을 이용해서 이미지에서 엣지를 검출합니다.

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 이진 이미지에서 컨투어(윤곽선)를 검출합니다.

# Find the largest contour
max_contour = max(contours, key = cv2.contourArea) 
# ------------
# Find bounding rectangle coordinates
x, y, w, h = cv2.boundingRect(max_contour)

# Crop image based on bounding rectangle coordinates
cropped_img = img[y : y + h, x : x + w]

# Save cropped image
cv2.imwrite(now.strftime("%m-%d_%H-%M(crop)") + ".png", cropped_img)
# 선택된 컨투어를 둘러싼 바운딩 박스를 추출하고, 해당 영역을 이미지에서 crop합니다. 그리고 crop된 이미지를 저장합니다.
# ------------
# Open cropped image
img = Image.open(savelocation)

# Convert image to grayscale
img_gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

# Threshold image to get binary inverse
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# Contour detection
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Extract individual cells from image
cells = []


for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if(w > 10 and h > 10):
        cells.append((x, y, w, h))

cnt = 0
# Crop each cell and save
for i in range(len(cells)):
    cell = cells[len(cells) - 1 - i]
    x, y, w, h = cell
    # Set bounding box to the entire cell
    x1, y1, x2, y2 = x, y, x + w, y + h
    crop_img = img.crop((x1, y1, x2, y2))
    width, height = crop_img.size
    
    if width > 50 and height < 400 and height > 50 and width < 600:
       cnt += 1
       crop_img.save(f"cell{cnt}.png")

    if height > 400 and width < 800:
        cnt += 1
        discode_print += "오늘은 공휴일!~"
        crop_img.save(f"cell{cnt}.png")
        holiday_List.append(cnt)

if holiday_List.count(2) == 1:  #월요일 공휴일
    day_plus += 1

if holiday_List.count(3) == 1:  #화요일 공휴일
    day_plus += 1

if holiday_List.count(4) == 1:  #수요일 공휴일
        day_plus += 1

if holiday_List.count(5) == 1:  #목요일 공휴일
        day_plus += 1

if holiday_List.count(6) == 1:  #금요일 공휴일
        day_plus += 1




# OCR 
for i in range(1, len(cells)):
    image_path = f"cell{i}.png"

    # Check if the image file exists
    if not os.path.exists(image_path):
        break

    image = Image.open(image_path).convert('L')  # 이미지를 그레이스케일로 변환
    text = pytesseract.image_to_string(image, lang='kor')
    discode_print += text

def get_output():
    output = discode_print
    return output