import os
import subprocess
from time import sleep
import speech_recognition as sr


#===[ INITIALIZE LISTENER ]===#
listener = sr.Recognizer()


#==[ LISTEN WITH MICROPHONE (NOT WORKING) ]==#

try:
    with sr.Microphone(device_index=0) as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except:
    print("Sorry, I didn't get that... Please repeat that for me.")
    pass

