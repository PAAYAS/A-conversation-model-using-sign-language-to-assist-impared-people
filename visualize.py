import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def visualize(audio_file):
    # Load audio file
    y, sr = librosa.load(audio_file)

    # Generate waveform plot
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title('Waveform plot')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

    # Generate mel-spectrogram plot
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mel_spec_db, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-spectrogram plot')
    plt.xlabel('Time (s)')
    plt.ylabel('Mel frequency')
    plt.show()