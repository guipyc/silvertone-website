import librosa
import pandas as pd
import pickle
import io


with open('audio.pkl', 'rb') as f:
    audio_lib = pickle.load(f)


data, samplerate = librosa.load(io.BytesIO(audio_lib))
print(len(data))
print(type(data))
