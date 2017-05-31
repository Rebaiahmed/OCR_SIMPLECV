import goslate
import inflect
import pyttsx
import pygame.camera
import pygame.image
from pygame.locals import *
import sys
from asprise_ocr_api import *
import pyttsx
from microsofttranslator import Translator
import re
import pyaudio
import speech_recognition as sr
from random import shuffle
import sys
from wit import Wit
import json
import fbchat
import pyaudio
import speech_recognition as sr








#***************define our functiosn here**********************************



#******************function to send message to facebook*****************

def sendMessageFacebook(msg) :
    client = fbchat.Client("ahmed.bouhmid94@gmail.com", "radhiabelhaj123A")

    friends = client.getUsers("Walid Khemiri")  # return a list of names
    friend = friends[0]
    sent = client.send(friend.uid, msg)
    if sent:
        print("Message sent successfully!")



#**********function to extract text from the image captured ***********
def ExtractText( ):

          Ocr.set_up()
          ocrEngine = Ocr()
          ocrEngine.start_engine("eng")
          s = ocrEngine.recognize("capture.jpg", -1, -1, -1, -1, -1,
                  OCR_RECOGNIZE_TYPE_ALL, OCR_OUTPUT_FORMAT_PLAINTEXT)
          #result = s;
          ocrEngine.stop_engine()
          return s



#*************Function to check arithmetic expressions contained in the text




def CheckArithmetic(str):
    # Code to determine if player wins
    if re.findall(r"([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)", str):
        return True

    return False



#************Eval arithmetic expresiions**********************

def Eval(expr):
         return  eval(expr)




#initializ the access token********************
access_token = 'GZ6AYYARVZP4526IY5NUHEMN7NBKRXJT'

#initialie the actions of the client****************

all_jokes = {
    'chuck': [
        'Chuck Norris counted to infinity - twice.',
        'Death once had a near-Chuck Norris experience.',
    ],
    'tech': [
        'Did you hear about the two antennas that got married? The ceremony was long and boring, but the reception was great!',
        'Why do geeks mistake Halloween and Christmas? Because Oct 31 === Dec 25.',
    ],
    'default': [
        'Why was the Math book sad? Because it had so many problems.',
    ],
}

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def merge(request):
    context = request['context']
    entities = request['entities']

    if 'joke' in context:
        del context['joke']
    category = first_entity_value(entities, 'category')
    if category:
        context['cat'] = category
    sentiment = first_entity_value(entities, 'sentiment')
    if sentiment:
        context['ack'] = 'Glad you liked it.' if sentiment == 'positive' else 'Hmm.'
    elif 'ack' in context:
        del context['ack']
    return context

def select_joke(request):
    context = request['context']

    jokes = all_jokes[context['cat'] or 'default']
    shuffle(jokes)
    context['joke'] = jokes[0]
    return context

actions = {
    'send': send,
    'merge': merge,
    'select-joke': select_joke,
}


actions = {
    'send': send,
    'merge': merge,
    'select-joke': select_joke,
}

#initializ our intelligence client************************
client = Wit(access_token=access_token, actions=actions)


#******************initializ the recognition service******************
#r=sr.Recognizer()
#r.energy_threshold=4000


#OPEN THE WEBCAM AND CAPTURE THE IMAGE*****************
pygame.camera.init()
#initialize*****************


#initialize the TRADUCTION api miccrosft******************

translator = Translator('ahmedrebai94', 'gD8d1De3IHbSFfwU68MAWzd+1Is9OHs1WE6muLFzay0=')

cameras = pygame.camera.list_cameras()
print "Using camera %s ..." % cameras[0]
webcam = pygame.camera.Camera(cameras[0])

webcam.start()

# grab first frame
img = webcam.get_image()

WIDTH = img.get_width()
HEIGHT = img.get_height()

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
pygame.display.set_caption("OCR application")


#initialize the audio library

#r=sr.Recognizer()
#r.energy_threshold=4000


while True :





    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            sys.exit()



    # draw frame
    screen.blit(img, (0,0))
    pygame.display.flip()
    # grab next frame
    img = webcam.get_image()




    result =''
    engine = pyttsx.init()

    for event in pygame.event.get():



         if event.type == pygame.KEYDOWN:
            print "clicked"
            pygame.image.save(img,"capture.jpg")
            result = ExtractText()

            print "the result is" + result

          #check if text contain arithmetci expressions****
            if CheckArithmetic(result)== True :
                print "arithmetic"
                if(Eval(result)):
                   print "extracted true" ,Eval(result)
                   output = Eval(result)
                   engine.say(output)
                   engine.runAndWait()
            else:
                   print "extracted false !"
                   print "simple text"

                   print "hi hi hi !"

                   resp = client.message(result)
                   print('Yay, got Wit.ai response: ' + str(resp) )
                   json_str = json.dumps(resp)
                   resp2 = json.loads(json_str)
                   print (resp['entities'])
                   resp3 = resp['entities']
                   print (resp3['intent'])
                   resp4 = resp3['intent'][0]['value']
                   print ( resp4)

                   if( result == "Walid see you 1* minutes later"):
                        client = fbchat.Client("ahmed.bouhmid94@gmail.com", "radhiabelhaj123A")

                        friends = client.getUsers("Walid Khemiri")  # return a list of names
                        friend = friends[0]
                        sent = client.send(friend.uid, "Message sent from pc")
                        if sent:
                           print("Message sent successfully!")



                   engine.say(resp4)
                   engine.runAndWait()






















#extract an element in the response









               #here we will apply chatbOt with facebbok wit.ai









               #audio recognition



           #translate the text
          #gs = goslate.Goslate()
          #text = gs.translate(result, 'fr')
          #print text
          #print translator.translate("HELLO", "Fr")
          #text =translator.translate(result, "Fr")




