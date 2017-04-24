# -*- coding: utf-8 -*-


import goslate
import pyttsx

# initialiser gogole traduction api
gs = goslate.Goslate()
# initialize audio library
engine = pyttsx.init()
text = gs.translate('hello world', 'fr')
print(gs.translate('hello world', 'fr'))

engine.say(text)
engine.runAndWait()
