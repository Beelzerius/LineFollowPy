import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='pt')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
    
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Diga alguma coisa")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data


data = recordAudio()
speak(data)
