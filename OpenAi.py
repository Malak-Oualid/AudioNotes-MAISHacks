from flask import Flask, request, render_template
import openai
from io import BytesIO
openai.api_key ="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"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend.html')  # assuming you have an index.html template

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
    print(transcript)
    return transcript

if __name__ == '__main__':
    app.run(debug=True)

