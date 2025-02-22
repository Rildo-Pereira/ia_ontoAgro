import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

class AudioFeatureExtractor:
    def extract_audio_features(self, audio_signal, sample_rate):
        """
        Extrai características importantes do sinal de áudio, como MFCCs, Mel Spectrogram e características temporais.

        Argumentos:
            audio_signal (numpy.ndarray): Sinal de áudio pré-processado.
            sample_rate (int): Taxa de amostragem do sinal.

        Retorna:
            dict: Um dicionário contendo as características extraídas (MFCC, Mel Spectrogram, RMS).
        """
        print("Extraindo características do áudio...")

        # **1. MFCC (Mel-Frequency Cepstral Coefficients)**
        # Os MFCCs representam a energia do sinal em diferentes bandas de frequência baseadas na escala Mel.
        # Isso é amplamente utilizado em tarefas como reconhecimento de fala.
        #Por padrão, 12-13 coeficientes são usados na maioria das aplicações de processamento de fala.
        #A taxa de amostragem do áudio (em Hz): indica quantas amostras por segundo o áudio possui (16 kHz, sr=16000)
        mfccs = librosa.feature.mfcc(y=audio_signal, sr=sample_rate, n_mfcc=13)
        print(f"MFCCs extraídos: {mfccs.shape[1]} frames com {mfccs.shape[0]} coeficientes")

        # **2. Mel Spectrogram**
        # Representação do espectro de frequências na escala Mel (mais próxima da percepção humana).
        # n_fft: Número de pontos para a Transformada Rápida de Fourier (FFT).
        # hop_length: Passo (número de amostras) entre janelas consecutivas.
        # n_mels: Número de bandas na escala Mel.

        mel_spectrogram = librosa.feature.melspectrogram(y=audio_signal, sr=sample_rate, n_fft=2048, hop_length=512, n_mels=128)
        mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)  # Converte para dB para melhor visualização

        # **3. RMS (Root Mean Square)**
        # Calcula a energia média em cada frame do áudio.
        rms = librosa.feature.rms(y=audio_signal)
        print(f"RMS extraído: {rms.shape[1]} frames")

        # **Visualizações**
        plt.figure(figsize=(14, 10))

        # MFCCs
        plt.subplot(3, 1, 1)
        librosa.display.specshow(mfccs, x_axis='time', sr=sample_rate, cmap='coolwarm')
        plt.colorbar()
        plt.title("MFCC (Mel-Frequency Cepstral Coefficients)")

        # Mel Spectrogram
        plt.subplot(3, 1, 2)
        librosa.display.specshow(mel_spectrogram_db, x_axis='time', y_axis='mel', sr=sample_rate, cmap='coolwarm')
        plt.colorbar()
        plt.title("Mel Spectrogram (em dB)")

        # RMS
        plt.subplot(3, 1, 3)
        plt.plot(rms[0], label="RMS")
        plt.xlabel("Frames")
        plt.ylabel("Amplitude RMS")
        plt.title("Energia RMS do Sinal")
        plt.legend()

        plt.tight_layout()
        plt.show()

        return {
            "MFCC": mfccs,
            "Mel Spectrogram": mel_spectrogram_db,
            "RMS": rms
        }