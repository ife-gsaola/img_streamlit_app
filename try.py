import streamlit as st
from gtts import gTTS
from io import BytesIO

def text_to_speech(text):
    if text:
        sound_file = BytesIO()
        tts = gTTS(text, lang='en')
        tts.write_to_fp(sound_file)
        st.audio(sound_file, format='audio/mp3', start_time=0, autoplay=True)

text = st.text_input("Enter text:")
if text:
    text_to_speech(text)
