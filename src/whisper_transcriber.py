from transformers import pipeline
from audio_processor import AudioProcessor

class WhisperTranscriber:
    def __init__(self):
        self.audio_processor = AudioProcessor()

    def speech_to_text_whisper(self, audio_path):
        """
        Usa o modelo Whisper para converter áudio em texto transcrito.
        Converte o áudio para WAV antes da transcrição para garantir a compatibilidade.
        Remove a especificação de idioma para usar a detecção automática ou o padrão do modelo.
        Retorna o texto transcrito.
        """
        print("Iniciando reconhecimento de fala com Whisper...")
        print(f"Arquivo de áudio original para transcrição (WhisperTranscriber): {audio_path}")

        # Converter para WAV usando AudioProcessor
        wav_audio_path = self.audio_processor.convert_to_wav(audio_path)
        print(f"Arquivo WAV para transcrição (WhisperTranscriber): {wav_audio_path}")

        # Carregar o pipeline do modelo Whisper (sem especificar o idioma)
        transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large")

        # Realizar a transcrição no arquivo WAV convertido (sem especificar o idioma)
        transcription = transcriber(wav_audio_path)["text"]

        print("Texto Transcrito (Whisper):", transcription)
        return transcription