import goslate
import inflect
import pyttsx
import pygame.camera
import pygame.image
import sys
from asprise_ocr_api import *

#OPEN THE WEBCAM AND CAPTURE THE IMAGE*****************

pygame.camera.init()

cameras = pygame.camera.list_cameras()

print "Using camera %s ..." % cameras[0]

webcam = pygame.camera.Camera(cameras[0])

webcam.start()

# grab first frame
img = webcam.get_image()

WIDTH = img.get_width()
HEIGHT = img.get_height()

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
pygame.display.set_caption("pyGame Camera View")

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            sys.exit()



    # draw frame
    screen.blit(img, (0,0))
    pygame.display.flip()
    # grab next frame
    img = webcam.get_image()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        #capture the image
        print "clicked"
        pygame.image.save(img,"capture.jpg")


#*********extract TEXT FROM IMAGE**************************

Ocr.set_up() # one time setup
ocrEngine = Ocr()
ocrEngine.start_engine("eng")
s = ocrEngine.recognize("capture.jpg", -1, -1, -1, -1, -1,
                  OCR_RECOGNIZE_TYPE_ALL, OCR_OUTPUT_FORMAT_PLAINTEXT)
print "Result: " + s

result = s;
# recognizes more images here ..
ocrEngine.stop_engine()



#***********translate text****************************









#*********if ARITHMETIC EXPRESSIONS THEN EVALUATE THEM and print the result
p = inflect.engine()
print p.number_to_words(1)




#***********TEXT TO SPEECH*******************

engine = pyttsx.init()
engine.say('ahmed.')
engine.runAndWait()
