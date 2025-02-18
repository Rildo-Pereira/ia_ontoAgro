from gtts import gTTS
import os

class VoiceSynthesizer:
    def synthesize(self, text: str):
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")