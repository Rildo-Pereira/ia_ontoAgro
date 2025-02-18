import whisper

class SpeechRecognizer:
    def __init__(self):
        self.model = whisper.load_model("base")

    def recognize(self) -> str:
        # Placeholder for actual audio input
        # audio_path = "path_to_audio_file.wav"
        audio_path = "testepizza.WAV"
        result = self.model.transcribe(audio_path)
        print(f'TEXTO: {result["text"]}')
        return result['text']