# This script will take care of recgonizing speech and converting it to text

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    print("Got it! Now to recognize it...")
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(audio)
        print("You said " + value)
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
