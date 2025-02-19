import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class TextSummarizer:
    def __init__(self):
        # Initialize Gemini model - assuming API key is configured in environment variables
        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def summarize_text(self, text_response: str, text_question: str) -> str:
        prompt_config = {
            "temperature": 0.5,
            "top_p": 1,
            "top_k": 32,
            "max_output_tokens": 100,
        }

        generation_config = genai.GenerationConfig(**prompt_config)

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]

        convo = self.model.start_chat(history=[])
        convo.generation_config = generation_config
        convo.safety_settings = safety_settings

        prompt = f"Crie uma resposta curta com base no texto em português brasileiro, o resumo tem que respoder a pergunta '{text_question}' com estilo do seguinte texto: {text_response} a saída tem que ser um texto curto, um paragrafo, legivel para leitura de dublagem e sem caracteres especiais"
        response = convo.send_message(prompt)
        return response.text