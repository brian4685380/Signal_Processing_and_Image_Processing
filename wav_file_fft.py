import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

wavefile = wave.open('../audios/sample-6s.wav', 'r')

fs = wavefile.getframerate()
num_frame = wavefile.getnframes()

str_data = wavefile.readframes(num_frame)
wave_data = np.frombuffer(str_data, dtype=np.int16)
wave_data = wave_data / (max(abs(wave_data)))
n_channel = 2
wave_data = np.reshape(wave_data, (num_frame, n_channel))

time = np.arange(0, num_frame) / fs
plt.plot(time, wave_data)
plt.show()

fft_data = abs(fft(wave_data[:, 1])) / fs
n0 = int(np.ceil(num_frame / 2))
fft_data1 = np.concatenate([fft_data[n0:num_frame], fft_data[0:n0]])
freq = np.concatenate([range(n0-num_frame, 0), range(0, n0)]) * fs / num_frame
plt.plot(freq, fft_data1)
plt.xlim(-1000, 1000)
plt.show()