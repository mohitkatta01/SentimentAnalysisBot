# This script will take care of recgonizing speech and converting it to text

import speech_recognition as sr
import time
import pyttsx3

def SpeechRecognize():
    # obtain audio from the microphone
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        try:
            # recognize speech using Google Speech Recognition
            audio = r.listen(source, timeout = 5)
            value = r.recognize_google(audio)
            print("You said " + value)
            return value
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! We couldn't process your request now; {0}").format(e)
        except sr.WaitTimeoutError:
            print("Timed out waiting for phrase")

def NamedEntityRecognition(text):
    # This function will take in the text and return the named entities
    # that are present in the text
    
    pass

def TextToSpeech(text):
    # This function will take in the text and convert it to speech
    engine = pyttsx3.init() # Initializing the pyttsx3 engine for TTS
    time.sleep(0.5)
    if "time" in text:
        text = "The time is " + time.strftime("%H:%M")

    engine.say(text)
    engine.runAndWait()

def main():
    
    text = SpeechRecognize()
    if (text == None):
        print("Try Again!")
    else:
        TextToSpeech(text)

if __name__ == "__main__":
    main()