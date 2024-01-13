#pip install gtts


from gtts import gTTS
import os

def text_to_speech():
    text = input("Enter your text here: ")
    tts = gTTS(text, lang='en', slow=False)

    name = input("Enter file name: ").strip().lower()
    name += ".mp3"
    tts.save(name)

    os.system(f"start {name}")

text_to_speech()