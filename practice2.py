#영어랑 한글이랑 같이 있는 경우 crop 해서 사용할 듯
from PIL import Image
import pytesseract
import cv2


img = Image.open('C:/Users/jhkim/OneDrive/바탕 화면/CodeCure/sangmyung restaurat.png')

crop_img1 = img.crop((142, 212, 310, 360))

crop_img1.show()

text = pytesseract.image_to_string(crop_img1, lang='kor')
print(text)