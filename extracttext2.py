import Image
import pytesseract
import Image
from PIL import Image, ImageEnhance, ImageFilter
im = Image.open("capture.jpg") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('capture.jpg')
text = pytesseract.image_to_string(Image.open('temp2.jpg'))
print(text)

#print pytesseract.image_to_string(Image.open('capture.jpg'))

