import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os

class AudioProcessor:
    def convert_to_wav(self, audio_path):
        """
        Converte um arquivo de áudio para o formato WAV e verifica se o arquivo foi criado, com tratamento de erros e logs detalhados.

        Argumentos:
            audio_path (str): Caminho para o arquivo de áudio de entrada.

        Retorna:
            str: Caminho para o arquivo WAV convertido ou o caminho original em caso de falha.
        """
        print(f"Iniciando conversão para WAV para o arquivo: {audio_path}")
        wav_path = ""
        try:
            print(f"Tentando carregar áudio com librosa: {audio_path}")
            y, sr = librosa.load(audio_path, sr=16000)
            print(f"Áudio carregado com sucesso. Taxa de amostragem: {sr}, Duração: {len(y) / sr:.2f} segundos")

            base, ext = os.path.splitext(audio_path)
            wav_path = base + ".wav"
            print(f"Caminho do arquivo WAV de saída: {wav_path}")

            print(f"Tentando salvar como WAV com soundfile: {wav_path}, Formato: WAV, Taxa de amostragem: {sr}")
            sf.write(wav_path, y, sr, format='WAV')
            print(f"Arquivo WAV salvo com sucesso em: {wav_path}")

            # Verificação extra se o arquivo WAV foi criado e não está vazio
            if os.path.exists(wav_path):
                if os.path.getsize(wav_path) > 0:
                    print(f"Arquivo WAV verificado e não vazio: {wav_path}")
                    return wav_path
                else:
                    error_message = f"Erro: Arquivo WAV criado está vazio: {wav_path}"
                    print(error_message)
                    os.remove(wav_path) # Remove o arquivo vazio
                    return audio_path # Retorna o original, conversão falhou
            else:
                error_message = f"Erro: Arquivo WAV não foi criado em: {wav_path}"
                print(error_message)
                return audio_path # Retorna o original, conversão falhou

        except librosa.LibrosaError as e_librosa:
            error_message = f"LibrosaError ao converter para WAV: {e_librosa}"
            print(error_message)
            return audio_path
        except sf.LibsndfileError as e_soundfile:
            error_message = f"LibsndfileError ao salvar WAV: {e_soundfile}"
            print(error_message)
            return audio_path
        except Exception as e:
            error_message = f"Erro desconhecido ao converter para WAV: {e}"
            print(error_message)
            return audio_path
        finally:
            if not wav_path and os.path.exists(wav_path): # Segurança extra para remover arquivos WAV possivelmente corrompidos
                try:
                    os.remove(wav_path)
                    print(f"Arquivo WAV incompleto/corrompido removido: {wav_path}")
                except Exception as remove_e:
                    print(f"Erro ao tentar remover arquivo WAV problemático {wav_path}: {remove_e}")
        return audio_path # Retorna o caminho original em caso de falha geral


    def preprocess_audio(self, audio_path):
        """
        Carrega o áudio, remove ruído simples (subtração de média) e normaliza o sinal.
        Retorna o sinal pré-processado e a taxa de amostragem.

        Argumentos:
            audio_path (str): Caminho para o arquivo de áudio a ser processado.

        Retorna:
            tuple: Um sinal de áudio pré-processado e a taxa de amostragem correspondente.
        """
        # Converter para WAV se o arquivo for m4a
        if audio_path.lower().endswith(".m4a"):
            audio_path = self.convert_to_wav(audio_path)

        # Carregar o áudio
        # `librosa.load` retorna o sinal de áudio (y) e a taxa de amostragem (sr).
        # Aqui, a taxa de amostragem é definida como 16kHz para ser compatível com a maioria dos modelos de ASR.
        print("Carregando o áudio para pré-processamento...")
        try:
            print(f"Carregando áudio com librosa: {audio_path}")
            y, sr = librosa.load(audio_path, sr=16000)  # Taxa de amostragem padrão 16kHz
            print(f"Áudio carregado com librosa com sucesso para pré-processamento. Taxa de amostragem: {sr}")
        except librosa.LibrosaError as e_load:
            print(f"LibrosaError ao carregar áudio para pré-processamento: {e_load}")
            raise e_load # Re-levando a exceção para interromper o processo se o áudio não puder ser carregado
        except Exception as e:
            print(f"Erro desconhecido ao carregar áudio para pré-processamento: {e}")
            raise e # Re-levando a exceção para interromper o processo se o áudio não puder ser carregado


        # Exibir informações básicas do áudio carregado
        print(f"Duração do áudio: {len(y) / sr:.2f} segundos")
        print(f"Taxa de amostragem: {sr} Hz")

        # Salvar o ruído original (média do sinal)
        ruido = np.mean(y)
        print(f"Ruído detectado (valor médio): {ruido:.4f}")

        # Remoção simples de ruído (subtração da média)
        # Esta etapa reduz o ruído estacionário removendo a média do sinal.
        # Isso é especialmente útil para eliminar desvios constantes que não representam a fala.
        print("Removendo ruído (subtração da média)...")
        y_denoised = y - ruido

        # Normalização
        # A normalização ajusta os valores de amplitude do sinal para ficarem dentro de uma faixa padrão.
        # Isso ajuda a evitar problemas de saturação e garante que regiões de baixa amplitude sejam destacadas.
        print("Normalizando o áudio...")
        y_normalized = librosa.util.normalize(y_denoised)

        # Análise estatística do sinal antes e depois da normalização
        print("Análise do sinal:")
        print(f"Amplitude original: Min={y.min():.4f}, Max={y.max():.4f}, Média={y.mean():.4f}")
        print(f"Amplitude sem ruído: Min={y_denoised.min():.4f}, Max={y_denoised.max():.4f}, Média={y_denoised.mean():.4f}")
        print(f"Amplitude normalizada: Min={y_normalized.min():.4f}, Max={y_normalized.max():.4f}, Média={y_normalized.mean():.4f}")

        # Plotar o áudio original, ruído e pré-processado
        # Visualizações úteis para comparar os efeitos do pré-processamento no sinal.
        print("Plotando o sinal de áudio...")
        plt.figure(figsize=(14, 12))

        # Sinal original
        plt.subplot(3, 1, 1)
        librosa.display.waveshow(y, sr=sr)
        plt.title("Áudio Original")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Amplitude")

        # Ruído detectado
        plt.subplot(3, 1, 2)
        plt.axhline(y=ruido, color="red", linestyle="--", label="Ruído Médio")
        librosa.display.waveshow(y, sr=sr, alpha=0.5)
        plt.title("Ruído Estacionário no Áudio")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Amplitude")
        plt.legend()

        # Sinal pré-processado
        plt.subplot(3, 1, 3)
        librosa.display.waveshow(y_normalized, sr=sr)
        plt.title("Áudio Pré-processado")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Amplitude")

        plt.tight_layout()
        plt.show()

        # Retornar o sinal pré-processado e a taxa de amostragem
        return y_normalized, sr