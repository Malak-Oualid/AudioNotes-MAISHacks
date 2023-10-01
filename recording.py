from pvrecorder import PvRecorder
import numpy as np
import wave, struct

for index, device in enumerate(PvRecorder.get_audio_devices()):
    print(f"[{index}] {device}")

recorder = PvRecorder(device_index=-1, frame_length=512)

try:
    recorder.start()

    while True:
        frame = recorder.read()
        # Do something ...
except KeyboardInterrupt:
    recorder.stop()
finally:
    recorder.delete()