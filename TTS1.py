

import speech_recognition as sr


r = sr.Recognizer()

audio = 'microphone-result.wav'

with sr.AudioFile(audio) as source:
    r.adjust_for_ambient_noise(source)
    print('SAY SOMETHING:');
    audio = r.record(source)
    print('PLEASE WAIT...')
    
try:
    print("TEXT: "+r.recognize_google(audio))
    print("Google thinks that you said:\n" + text)
    
except:
    pass;