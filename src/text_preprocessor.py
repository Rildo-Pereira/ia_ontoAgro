import re

class TextPreprocessor:
    def preprocess_text(self, text):
        """
        Realiza o pré-processamento do texto, convertendo para lowercase e removendo pontuação.

        Argumentos:
            text (str): Texto a ser pré-processado.

        Retorna:
            str: Texto pré-processado.
        """
        text = text.lower().strip()  # Lowercase
        #remove todos os caracteres que não sejam letras, números ou espaços da string text
        text = re.sub(r"[^\w\s]", "", text)  # Remover pontuação
        return text