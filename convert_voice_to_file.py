import pyaudio
import soundfile as sf
import numpy as np
import os

# Set the audio parameters
sample_rate = 44100  # You can adjust this based on your preferences
audio_duration = 10   # Duration of the recording in seconds
output_file = "output_audio.mp3"  # Replace with your desired output file name

# Initialize the audio stream
audio = pyaudio.PyAudio()
def record_to_file():
    # Open a microphone stream
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=1024)

    print("Recording...")

    # Initialize an empty list to store audio data
    audio_data = []

    # Record audio for the specified duration
    for i in range(0, int(sample_rate / 1024 * audio_duration)):
        data = stream.read(1024)
        audio_data.append(data)

    print("Recording complete.")

    # Close the microphone stream and audio object
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Check if audio data is empty
    if not audio_data:
        print("No audio data recorded.")
    else:
        # Concatenate and save the recorded audio as an MP3 file
        audio_bytes = b''.join(audio_data)
        sf.write(output_file, np.frombuffer(audio_bytes, dtype=np.int16), sample_rate)
        print(f"Audio saved to {output_file}")


    # Get the absolute path of the created file
    file_path = os.path.abspath("/Users/karineha/projet/flaskProject/output_audio.mp3")

    # Print the file path
    print(f"File '{output_file}' created at: {file_path}")
    return file_path

record_to_file()