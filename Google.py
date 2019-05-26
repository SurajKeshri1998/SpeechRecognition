# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:19:33 2019

@author: user
"""

import speech_recognition as sr
import webbrowser as wb

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('SAY SOMETHING:');
    audio = r.listen(source)
    print('PLEASE WAIT...')
    
try:
    text = r.recognize_google(audio)
    print("You Said: \n" + text)
    wb.get(chrome_path).open(text)
except:
    pass;
    