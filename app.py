import streamlit as st
import requests
import pandas as pd
import numpy as np
import librosa
from audio_recorder_streamlit import audio_recorder
from audiorecorder import audiorecorder
import pickle
import IPython.display as ipd
from scipy.io.wavfile import write
import pickle
import io
import os
import time
#import pyrebase

#config = {"apiKey": "AIzaSyDKRTugV9mU0QJHrEhAT_yBYU6HcrASlxg",
#  "authDomain": "silvertone-batch1011.firebaseapp.com",
#  "projectId": "silvertone-batch1011",
#  "storageBucket": "silvertone-batch1011.appspot.com",
#  "messagingSenderId": "909112813098",
#  "appId": "1:909112813098:web:21b613c427ae95667a4553",
#  "measurementId": "G-RZHFZL7BRF"}
#
#firebase = pyrebase.initialize_app(config)
#storage = firebase.storage()
#path_on_cloud = 'audio/audio.pkl'
#path_local = 1
#
#auth = firebase.auth()
#
## Log the user in
#user = auth.sign_in_with_email_and_password(guilhermeofficial.35@gmil.com, password)
#
## Get a reference to the database service
#db = firebase.database()
#
## Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])"""



base="light"

from datetime import datetime
filename = None
now = datetime.now() # current date and time
date_time = now.strftime("%Y_%m_%d_%H_%M_%S")
#print("date and time:",date_time
st.title("Silvertone!")
#st.header("Record a 5 seconds audio, and receive a % ....")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


st.sidebar.title("Welcome to Silvertone!")
st.sidebar.image("logo2.png", use_column_width=True)
st.sidebar.text("Contributors:")
st.sidebar.text("Luiz Lianza")
st.sidebar.text("Victor Sattamini ")
st.sidebar.text("Lucas Gama")
st.sidebar.text("Guilherme Barreto")


import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('logo2.png')



#status_text.text('Done!')
#st.balloons()

#st.set_page_config(layout="wide")
#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
#    # To read file as bytes:
#    bytes_data = uploaded_file.getvalue()
#    st.write(bytes_data)
#st.markdown('or')
audio_bytes = audio_recorder()
if audio_bytes:
    st.audio(audio_bytes, format='audio/wav')
    filename = (f'{date_time}audio.pkl')
    #storage.child(path_on_cloud).push(audio_bytes)
    pickle.dump(audio_bytes, open(filename, 'wb'))

if filename is not None:
    with open(filename, 'rb') as f:
        audio_lib = pickle.load(f)
        data, samplerate = librosa.load(io.BytesIO(audio_lib))
        #col1, col2, col3,col4 = st.columns(4)
        #col1.metric("Happiness", "","34%")
        #col2.metric("Surprise", "9 %","34")
        #col3.metric("Neutral", "54%")
        #col4.metric("Sad", "1%")

        #st.markdown(len(data))
        os.remove(filename)
        #st.markdown(len(data))
        #st.markdown(type(data))
        #st.markdown(filename)

    #pickle.dump(audio_bytes, open(filename, 'wb'))
#    wav_file = open("audio.mp3", "wb")
#    wav_file.write(audio_bytes.tobytes())
    #sample,sr = librosa.core.load(audio_bytes)
    #ipd.Audio(sample)
    #audio = st.audio(audio_bytes, format="audio/wav")
    #st.markdown(audio_bytes)
    #scipy.io.wavfile.write(filename, rate, data)
    #filename = 'audio.wav'
    #pickle.dump(audio_bytes, open(filename, 'wb'))
    #urllib.request.urlretrieve('http://localhost:8501/media/ea89cb71a0175954e7bbaf5c2a00fec7717d2268080a96b03b3e24f8.wav', 'audio.wav')
    #ipd.Audio(filename)
    #ipd.Audio('audio.wav'[5])



#sample,sr = librosa.core.load(audio.wav)
#iipd.Audio(sample)
#
#from io import BytesIO
#import urllib
#from pydub import AudioSegment


#st.title("Audio Recorder")
#audio = audiorecorder("Click to record", "Recording...")
#
#if len(audio) > 0:
#    # To play audio in frontend:
#    st.audio(audio)
#
#    # To save audio to a file:
#    wav_file = open("audio.mp3", "wb")
#    wav_file.write(audio.tobytes())
#    #sample, sr = librosa.load(audio)
#    #ipd.Audio(sample)
#    #sample,sr = librosa.core.load('audio.mp3')
#    #ipd.Audio(sample)
