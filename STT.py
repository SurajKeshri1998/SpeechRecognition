# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:05:52 2019

@author: user
"""

import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('SAY SOMETHING:');
    audio = r.listen(source)
    print('PLEASE WAIT...')
    
try:
    print("TEXT: "+r.recognize_google(audio , language = 'hi-IN'))
    print("TEXT: "+r.recognize_google(audio))
    print("Google thinks that you said:\n" + text)
except:
    pass;