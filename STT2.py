# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:00:26 2019

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
    print("TEXT: "+r.recognize_google(audio))
    print("Audio Successfully Recorded!!! Check File Directory")
    print("Google thinks that you said:\n" + text)
    wb.get(chrome_path).open(text)
except:
    pass;
    

with open("microphone-result.wav","wb") as f:
    f.write(audio.get_wav_data())
    
with open("microphone-result.aiff","wb") as f:
    f.write(audio.get_aiff_data())
    
with open("microphone-result.flac","wb") as f:
    f.write(audio.get_flac_data())
    