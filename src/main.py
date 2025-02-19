from ia_ontoAgro.src.speech_recognizer import SpeechRecognizer
from ia_ontoAgro.src.ontology_query import OntologyQuery
from ia_ontoAgro.src.voice_synthesizer import VoiceSynthesizer
from ia_ontoAgro.src.text_summarizer import TextSummarizer

class MainApp:
    def __init__(self):
        self.speech_recognizer = SpeechRecognizer()
        self.ontology_query = OntologyQuery("OntologiaClimaAgriculturaV4.rdf")
        # self.ontology_query = OntologyQuery("pizza.owl")
        self.voice_synthesizer = VoiceSynthesizer()

    def run(self, audio_path: str, output_path: str):
        print("Listening for voice command...")
        command = self.speech_recognizer.recognize(audio_path)
        print(f"Recognized command: <<<<{command}>>>>")

        response = self.ontology_query.query(command)
        print(f"Ontology response: <<<<{response}>>>>")

        summarizer = TextSummarizer()
        text_resume = summarizer.summarize_text(response, command)
        print(f"Text Resume: <<<<{text_resume}>>>>")

        self.voice_synthesizer.synthesize(text_resume, output_path)

if __name__ == "__main__":
    fileName = 'P9'
    app = MainApp()
    app.run(audio_path=f"{fileName}.m4a", output_path=f"{fileName}.mp3")