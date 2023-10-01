from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize_and_store_speech():
    try:
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Open the microphone and start listening for speech
        with sr.Microphone() as source:
            print("Listening... Say something:")
            audio = recognizer.listen(source)

        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

        # Store the recognized text in a file
        with open("speech_recognition_output.txt", "w") as file:
            file.write(text)

        print("Speech recognition results saved to 'speech_recognition_output.txt'")
        return jsonify({'message': 'Speech recognition completed.'})
    except sr.UnknownValueError:
        return jsonify({'error': 'Sorry, I could not understand what you said.'}), 400
    except sr.RequestError as e:
        return jsonify({'error': f'Sorry, there was an error with the request: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
