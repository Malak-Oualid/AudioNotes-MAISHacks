#from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template
import speech_recognition as sr

def recognize_and_store_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Open the microphone and start listening for speech
    with sr.Microphone() as source:
        print("Listening... Say something:")
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

        # Store the recognized text in a file
        with open("speech_recognition_output.txt", "w") as file:
            file.write(text)

        print("Speech recognition results saved to 'speech_recognition_output.txt'")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the request: {str(e)}")
    return text

