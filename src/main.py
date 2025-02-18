from speech_recognizer import SpeechRecognizer
from ontology_query import OntologyQuery
from voice_synthesizer import VoiceSynthesizer

class MainApp:
    def __init__(self):
        self.speech_recognizer = SpeechRecognizer()
        # self.ontology_query = OntologyQuery("OntologiaClimaAgricultura.owx")
        self.ontology_query = OntologyQuery("pizza.owl")
        self.voice_synthesizer = VoiceSynthesizer()

    def run(self):
        print("Listening for voice command...")
        command = self.speech_recognizer.recognize()
        print(f"Recognized command: {command}")

        response = self.ontology_query.query(command)
        print(f"Ontology response: {response}")

        self.voice_synthesizer.synthesize(response)

if __name__ == "__main__":
    app = MainApp()
    app.run()