import pyaudio
import pyttsx3
import random
import sys
import speech_recognition as sr

engine = pyttsx3.init() # object creation

#Set list of greenting and get randomly from it
greetings = ["ohh hi body", "Hello", "Hi pal", "Good morning", "Hello, how are you"]
#Set list of mood and get randomly from it
mood = ["Not bad", "Good, thanks", "Not so bad", "Fine, thank you", "Good, how are you?"]

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male, 1 for female

myRecognizer = sr.Recognizer()
mic = sr.Microphone(device_index=1)
# For cycle to print the available microphones. Uncomment the next two lines to print the list
# for x in range(len(sr.Microphone.list_microphone_names())):
#     print(str(x)+":"+sr.Microphone.list_microphone_names()[x])
while True:
    with sr.Microphone() as source:
        # Filter the ambient noises. It is helps to understand better wht you speak
        myRecognizer.adjust_for_ambient_noise(source)
        print("Say Something")
        engine.say("Say Something")
        engine.runAndWait()
        audio=myRecognizer.listen(source)
        print("...")
    try:
        print(myRecognizer.recognize_google(audio),"\n")
        order = myRecognizer.recognize_google(audio)
        if order == "play music" or order == "music":
            print("Go to Youtube :D")
        elif order == "hi" or order == "hello":
            g = random.randint(0, len(greetings))
            engine.say(greetings[g])
            engine.runAndWait()
        elif order == "how are you":
            g = random.randint(0, len(mood))
            engine.say(mood[g])
            engine.runAndWait()
        elif order == "who are you":
            print("I am an deaf idiot!")
            engine.say("I am an deaf idiot!")
            engine.runAndWait()
        elif order == "exit" or order == 'quit':
            print('Good bye!')
            sys.exit(0)
        else:
            continue
            
    except:
        pass
