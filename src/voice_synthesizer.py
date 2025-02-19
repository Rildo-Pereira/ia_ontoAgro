from gtts import gTTS
import os

class VoiceSynthesizer:
    def synthesize(self, text: str, output_path: str):
        tts = gTTS(text=text, lang='pt')
        tts.save(output_path)
        # os.system("mpg321 response.mp3")