from flask import Flask, request, render_template
from views import views
import openai
from io import BytesIO
import subprocess
import numpy as np
import convert_voice_to_file as cvf
import speeech_rec
openai.api_key ="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"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend.html')  # assuming you have an index.html template

@app.route('/run_record', methods=['GET'])
def run_record():
    return cvf.record_to_file()

@app.route('/run_speech', methods=['GET'])
def run_speech():
    user_transcript = speeech_rec.recognize_and_store_speech().split(" ")
    with open("uploaded_script.txt")as buffer:
        song_lyrics = buffer.readline()
    song_lyrics = song_lyrics.split(" ")
    resp = []
    for i, word in enumerate(user_transcript):
        song_word = song_lyrics[i]
        if song_word.lower() == word.lower():
            resp.append(f"correct word!: {song_word}")
        else:
            resp.append(f"worng! correct word is: {song_word} you said {word}")
    return resp


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
        # Create a file-like object in memory
    in_memory_file = BytesIO()
    in_memory_file.name = file.filename  # Set the name attribute
    in_memory_file.write(file.read())  # Write the file data into the in-memory file
    in_memory_file.seek(0)  # Seek to the beginning of the file
    transcript = openai.Audio.transcribe(
        file=in_memory_file,
        model="whisper-1",
        response_format="text",
        language="en"
    )
    with open("uploaded_script.txt", "w") as buffer:
        buffer.write(transcript)
    return transcript

if __name__ == '__main__':
    app.run(debug=True)

