from PIL import Image, ImageEnhance

# Load the image
img = Image.open("C:/Users/jhkim/OneDrive/바탕 화면/CodeCure/test_brightness.png")

# Adjust the brightness
brightness_factor = 1.5  # Increase the brightness by 50%
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(brightness_factor)

# Save the result
img.save("C:/Users/jhkim/OneDrive/바탕 화면/test_brightness.png")