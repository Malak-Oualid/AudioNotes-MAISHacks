import librosa

# Path to your MP3 audio file
audio_file = "/Users/karineha/projet/flaskProject/static/Music/Laufey_-_Magnolia_Official_Audio.mp3"

# Load the audio file
y, sr = librosa.load(audio_file)

# Estimate pitch using the Harmonic/Percussive source separation method
harmonic, percussive = librosa.effects.hpss(y)
pitches, magnitudes = librosa.core.piptrack(y=harmonic, sr=sr)

# Extract the pitch from the magnitudes
pitch_values = []
for t in range(magnitudes.shape[1]):
    index = magnitudes[:, t].argmax()
    pitch_values.append(pitches[index, t])

# Print each extracted pitch value on a new line
for pitch in pitch_values:
    print(f"Pitch: {pitch:.2f} Hz")