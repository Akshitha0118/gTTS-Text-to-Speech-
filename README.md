# gTTS-Text-to-Speech-
# 🎙️ Text-to-Speech using gTTS (Google Text-to-Speech)

This project demonstrates how to convert text into speech using the **gTTS** (Google Text-to-Speech) library in Python and play the generated audio using **IPython.display.Audio**.

---

## 📌 Features
- Convert custom text into speech
- Save as `.wav` audio file
- Play audio directly inside Jupyter Notebook

---

## 🧩 Requirements

Install the required libraries:

pip install gTTS
pip install IPython

---
## 🧾 Source Code
from gtts import gTTS
from IPython.display import Audio

#Convert Text to Speech
text = gTTS('welcome to nareshit datascience prakash senapati 9am class')

#Save Audio File
text.save('text_gtts.wav')

#Play Audio in Notebook
sound_file = 'text_gtts.wav'
Audio(sound_file, autoplay=False)

---
## 📁 Output

- A speech audio file named text_gtts.wav will be created.

- Click Play ▶️ inside the Jupyter Notebook to listen to the speech.

## 🚀 How to Run

- Copy the above Python script into a Jupyter Notebook or .py file

- Run the script

- Play the audio output file generated
