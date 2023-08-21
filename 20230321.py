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


driver = webdriver.Chrome("C:/Users/jhkim/Downloads/chromedriver_win32/chromedriver.exe")

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

savelocation = "C:/Users/jhkim/0315pr.png" #내 컴퓨터의 저장 위치 _ 디버깅할 때마다 매번 파일명 변경해야됨.
urllib.request.urlretrieve(img_url, savelocation) #해당 url에서 이미지를 다운로드 메소드

# # OCR 기법 사용
img = Image.open(savelocation)
img.show()

crop_img_mon = img.crop((142, 212, 308, 356))
crop_img_tue = img.crop((308, 212, 497, 356))
crop_img_wed = img.crop((497, 212, 690, 356))
crop_img_thu = img.crop((690, 212, 868, 356))
crop_img_fri = img.crop((868, 212, 1035, 356))

# crop_img_mon.show()
# crop_img_tue.show()
# crop_img_wed.show()
# crop_img_thu.show()
# crop_img_fri.show()

print(pytesseract.image_to_string(crop_img_mon, lang='kor'))
print(pytesseract.image_to_string(crop_img_tue, lang='kor'))
print(pytesseract.image_to_string(crop_img_wed, lang='kor'))
print(pytesseract.image_to_string(crop_img_thu, lang='kor'))
print(pytesseract.image_to_string(crop_img_fri, lang='kor'))