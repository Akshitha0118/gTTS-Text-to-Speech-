import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

# Streamlit Frontend Title
st.title("🎤 Text to Speech Generator")
st.write("Convert your text into speech with different language options!")

# Input Text
text_input = st.text_area("Enter the text you want to convert to speech:", placeholder="Type something here...")

# Language Selection
language = st.selectbox(
    "Select Language:",
    ("English", "Hindi", "Telugu", "Tamil")
)

language_code = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta"
}

# Audio Format
audio_format = st.radio("Choose Audio Format", ("MP3", "WAV"))

# Generate Button
if st.button("Generate Audio 🎶"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text before generating audio!")
    else:
        tts = gTTS(text=text_input, lang=language_code[language])
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)

        if audio_format == "MP3":
            file_name = "output.mp3"
            mime = "audio/mpeg"
        else:
            file_name = "output.wav"
            mime = "audio/wav"

        st.audio(audio_file, format=mime)

        # Download Button
        st.download_button(
            label="Download Audio",
            data=audio_file,
            file_name=file_name,
            mime=mime,
        )

st.markdown("---")
st.write("Developed for Naresh IT | Data Science | Prakash Senapati Sir | 9 AM Batch 🎓")
