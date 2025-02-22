import whisper
import spacy
from whisper_transcriber import WhisperTranscriber
from text_preprocessor import TextPreprocessor
from audio_processor import AudioProcessor


class SpeechRecognizer:
    def __init__(self):
        self.model = whisper.load_model("base")
        self.whisper_transcriber = WhisperTranscriber()
        self.text_preprocessor = TextPreprocessor()
        self.audio_processor = AudioProcessor() # Inicializa AudioProcessor

    def recognize(self, audio_path: str) -> str:
        # Converter para WAV antes de processar
        wav_audio_path = self.audio_processor.convert_to_wav(audio_path)
        print(f"Arquivo WAV gerado (SpeechRecognizer): {wav_audio_path}") # Log do caminho WAV

        # Carregar modelo de NLP do spaCy para português
        nlp = spacy.load("pt_core_news_lg")

        result = self.whisper_transcriber.speech_to_text_whisper(wav_audio_path) # Usa o caminho WAV
        # Aplicar pré-processamento de texto usando TextPreprocessor
        result_preprocessed = self.text_preprocessor.preprocess_text(result)
        doc = nlp(result_preprocessed)
        print("Texto Pré-processado:", result_preprocessed)
        return result_preprocessed