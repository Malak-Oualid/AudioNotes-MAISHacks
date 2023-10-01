import requests
import json
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key ="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"


def transcribe_audio(audio_path):
    # Define the API endpoint for the Whisper ASR system
    endpoint = 'https://api.openai.com/v1/whisper/recognize'

    # Read the audio file
    with open(audio_path, 'rb') as audio_file:
        audio_data = audio_file.read()

    # Set the request headers, including the API key
    headers = {
        'Authorization': f'Bearer {openai.api_key}',
        'Content-Type': 'audio/wav',
    }

    # Make the API request to transcribe the audio
    response = requests.post(endpoint, headers=headers, data=audio_data)

    if response.status_code == 200:
        result = json.loads(response.text)
        return result['text']
    else:
        return None

def create_html_transcription(transcription):
    # Generate an HTML document to display the transcription
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Whisper ASR Transcription</title>
    </head>
    <body>
        <h1>Transcription:</h1>
        <p>{transcription}</p>
    </body>
    </html>
    """

    # Save the HTML content to a file
    with open("transcription.html", "w") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    audio_path = '/Users/karineha/projet/flaskProject/static/Music/DANGEROUS_WOMAN_-_Ariana_Grande_Travis_Garland_Cover_320_kbps.mp3'  # Replace with the path to your audio file
    transcription = transcribe_audio(audio_path)

    if transcription:
        create_html_transcription(transcription)
        print("HTML file saved as 'transcription.html'")
    else:
        print("Transcription failed.")