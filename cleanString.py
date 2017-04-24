# -*- coding: utf-8 -*-
import re
import goslate
import enchant

gs = goslate.Goslate()

my_str = """ RAPPORT DE STAGE PU,
DE MAS‘l-ERE “*&5;ng
EN ‘ MEL ‘
mg RIBUTION ET NEGOCIATIQN m
. Mil*‘u
La fidélisation des cliems dansum
librairie On line
(Cas dc «L’univers du livrc») """

my_new_string = re.sub('[^a-zA-Z0-9 \n\.]', '', my_str)

words = my_new_string.split()

#print "string after substring is " + my_new_string

for idx, word in enumerate(words):
    #check
    print  word

#TRANSLATE TEXT***********************
#print(gs.translate(words, 'en'))
