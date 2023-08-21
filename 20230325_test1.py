import easyocr
reader = easyocr.Reader(['ko','en']) # this needs to run only once to load the model into memory
result = reader.readtext('C:/Users/jhkim/OneDrive/바탕 화면/CodeCure/sangmyung restaurat.png') 