from PIL import Image
import zbar
import cv2.cv as cv

capture = cv.CaptureFromCAM(1)
imgSize = cv.GetSize(cv.QueryFrame(capture))
img = cv.QueryFrame(capture)

#SOMETHING GOES HERE TO TURN FRAME INTO IMAGE
img = img.convert('L')
width, height = img.size

scanner = zbar.ImageScanner()
scanner.parse_config('enable')
zbar_img = zbar.Image(width, height, 'Y800', img.tostring())

# scan the image for barcodes
scanner.scan(zbar_img)

for symbol in zbar_img:
    print symbol.dat
