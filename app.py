import streamlit as st
from utils import text_to_speech, autoplay_audio, speech_to_text
from audio_recorder_streamlit import audio_recorder


st.title("Voice to Voice translations")
st.markdown("""
<style>
.big-font {
    font-size:24px !important;
    color: #e8b62c;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Translate other language to english with audio script.</p>', unsafe_allow_html=True)
# st.sidebar.header("Enter OpenAI Key(**Not store anywhere**)")
# api_key = st.sidebar.text_input("Enter your openai keys", type="password")
# client = OpenAI(api_key=api_key)


audio = st.file_uploader("Upload an audio file and wait for results", type=["mp3","wav","mp4"])
if audio is not None:
    transcript = speech_to_text(audio)
    if transcript:
        st.write(transcript)
        with st.spinner("Generating audio response..."):    
            audio_file = text_to_speech(transcript)
            autoplay_audio(audio_file)
    


