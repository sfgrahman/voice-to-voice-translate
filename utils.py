from openai import OpenAI 
import os 
from dotenv import load_dotenv, find_dotenv
import base64
import streamlit as st

load_dotenv(override=True)
api_key =  os.environ.get("OPENAI_API_KEY")
#print(api_key)
client = OpenAI(api_key=api_key)

def speech_to_text(audio_data):
    transcript = client.audio.translations.create(
            model="whisper-1",
            response_format="text",
            file=audio_data
        )
    return transcript


def text_to_speech(input_text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=input_text
    )
    webm_file_path = "temp_audio_play.mp3"
    with open(webm_file_path, "wb") as f:
        response.stream_to_file(webm_file_path)
    return webm_file_path


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)