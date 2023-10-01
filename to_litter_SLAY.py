import librosa
import numpy as np
import convert_voice_to_file as cvf

def compare_audio_files(audio_file1, audio_file2):
    # Load audio files
    y1, sr1 = librosa.load(audio_file1)
    y2, sr2 = librosa.load(audio_file2)

    # Extract spectrograms
    spectrogram1 = np.abs(librosa.stft(y1))
    spectrogram2 = np.abs(librosa.stft(y2))

    # Ensure both spectrograms have the same number of columns (time frames)
    min_frames = min(spectrogram1.shape[1], spectrogram2.shape[1])
    spectrogram1 = spectrogram1[:, :min_frames]
    spectrogram2 = spectrogram2[:, :min_frames]

    # Calculate the difference spectrogram
    difference_spectrogram = abs(((spectrogram1 - spectrogram2) / spectrogram1) * 100)

    # Flatten the difference spectrogram and convert it to a list
    difference_list = difference_spectrogram.flatten().tolist()

    return difference_list


# Paths to audio files for comparison
audio_file1 = cvf.record_to_file()
audio_file2 = "/Users/karineha/projet/flaskProject/static/Music/Laufey_-_Magnolia_Official_Audio.mp3"

# Get the list of differences
difference_list = compare_audio_files(audio_file1, audio_file2)


# Print each difference on a separate line
def do():
    sum_all_difference = 0
    difference_count = 0
    for i in range(len(difference_list)):
        print("Difference:", difference_list[i])
        if type(difference_list[i]) == float:
            if difference_list[i] < 100:
                sum_all_difference += difference_list[i]
                difference_count += 1

    average_difference = sum_all_difference / difference_count
    return str(average_difference)


average_difference = do()
def message_voice_accuracy(average_difference):

    print("Average Difference:", float(average_difference))
    if 50 < float(average_difference):
        print("This was not a cover. It was a creation of a whole other song")
    elif 50 >= float(average_difference) > 20:
        print("I heard better cover of songs, not gonna lie.")
    elif 10 <= float(average_difference) < 20:
        print("You sang well. Keep going! or don't...")
    elif 5 <=float(average_difference) < 10:
        print("Wow! Okay vocalist.")
    elif float(average_difference) < 5:
        print("Devoured the cover. The song is yours now.")

message_voice_accuracy(average_difference)
