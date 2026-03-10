import numpy as np
import matplotlib.pyplot as plt

# 1. Simulação do "Mundo Real" (Sinal Analógico)
frequencia_sinal = 10  # 10 Hz
t_continuo = np.linspace(0, 1, 1000) # 1000 pontos em 1 segundo
sinal_analogico = np.sin(2 * np.pi * frequencia_sinal * t_continuo)

# 2. O Conversor A/D (Amostragem)
fs = 30  # Frequência de amostragem: 30 amostras por segundo
t_amostrado = np.arange(0, 1, 1/fs)
sinal_digital = np.sin(2 * np.pi * frequencia_sinal * t_amostrado)

# Visualização
plt.plot(t_continuo, sinal_analogico, label='Analógico (Original)')
plt.stem(t_amostrado, sinal_digital, 'r', label='Digital (Amostrado)')
plt.legend()
plt.show()