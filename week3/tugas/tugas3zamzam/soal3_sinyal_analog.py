import numpy as np
import matplotlib.pyplot as plt

# Generate time array (0 sampai 2 detik, 2000 titik)
t = np.linspace(0, 2, 2000)

# Generate noise dengan standar deviasi 0.3
noise = 0.3 * np.random.randn(len(t))

# Sinyal bersih (tanpa noise)
clean_signal = 3 * np.sin(2 * np.pi * 4 * t + 0) + 2 * np.cos(2 * np.pi * 6 * t + np.pi/4)

# Sinyal dengan noise
noisy_signal = clean_signal + noise

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(t, clean_signal, label='Sinyal Bersih', linewidth=2, color='blue')
plt.plot(t, noisy_signal, label='Sinyal + Noise', alpha=0.7, color='orange')

# Styling sesuai soal
plt.title('Sinyal Analog: Kombinasi Sin & Cos dengan Noise')
plt.xlabel('Waktu (detik)')
plt.ylabel('Amplitudo')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()