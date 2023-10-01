import whisper

model = whisper.load_model("base")
result = model.transcribe("Ariana_Grande_-_Dangerous_Woman_Audio.mp3")

with open("transcription.txt", "w") as f:
    f.write(result["text"])