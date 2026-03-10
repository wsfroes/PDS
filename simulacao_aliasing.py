import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# ==========================================
# CONFIGURAÇÕES DO "MUNDO ANALÓGICO"
# ==========================================
Fs_analogico = 1000  
t = np.arange(0, 1, 1/Fs_analogico) 

freq_util = 5   
freq_ruido = 90 

sinal_util = np.sin(2 * np.pi * freq_util * t)
ruido = 0.5 * np.sin(2 * np.pi * freq_ruido * t)
sinal_real = sinal_util + ruido 

# ==========================================
# CONFIGURAÇÕES DO "MUNDO DIGITAL"
# ==========================================
Fs_digital = 40
salto = int(Fs_analogico / Fs_digital) 
t_digital = t[::salto]

# Passo 2: O Desastre (Aliasing)
sinal_aliasing = sinal_real[::salto]

# Passo 3: Filtro Anti-Aliasing
freq_corte = 20
nyquist = Fs_analogico / 2
corte_normalizado = freq_corte / nyquist
b, a = butter(4, corte_normalizado, btype='low')
sinal_filtrado_analogico = lfilter(b, a, sinal_real)

# Passo 4: Amostragem Segura
sinal_digital_seguro = sinal_filtrado_analogico[::salto]

# ==========================================
# GERANDO OS GRÁFICOS EM JANELAS SEPARADAS
# ==========================================

# Configuração comum: figsize=(10, 6) torna o gráfico mais alto
altura_grafico = (10, 6)

# Janela 1: Mundo Real
plt.figure("Janela 1 - Mundo Real", figsize=altura_grafico)
plt.plot(t, sinal_real, color='gray')
plt.title("Print 1: O Mundo Real (Sinal Útil 5Hz + Ruído 90Hz)")
plt.xlim(0, 0.5)
plt.grid(True)

# Janela 2: O Desastre (Aliasing) com legenda fora
plt.figure("Janela 2 - Aliasing", figsize=altura_grafico)
plt.plot(t, sinal_util, color='lightgray', linestyle='dashed', label='Sinal Real (5Hz)')
plt.plot(t_digital, sinal_aliasing, 'ro-', label='Sinal Digital (Aliasing)')
plt.title("Print 2: A Falha! (Amostragem sem Filtro criando onda fantasma)")
plt.xlim(0, 0.5)
# bbox_to_anchor joga a legenda para fora do eixo do gráfico
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout() # Garante que a legenda fora não seja cortada

# Janela 3: O Filtro Anti-Aliasing
plt.figure("Janela 3 - Filtro", figsize=altura_grafico)
plt.plot(t, sinal_filtrado_analogico, color='blue')
plt.title("Print 3: A Solução Física (Sinal após o Filtro Anti-Aliasing)")
plt.xlim(0, 0.5)
plt.grid(True)

# Janela 4: Amostragem Segura
plt.figure("Janela 4 - Amostragem Correta", figsize=altura_grafico)
plt.plot(t, sinal_filtrado_analogico, color='lightgray', linestyle='dashed')
plt.plot(t_digital, sinal_digital_seguro, 'go-', label='Sinal Digital (Correto)')
plt.title("Print 4: Amostragem Segura (O computador entende a realidade)")
plt.xlim(0, 0.5)
plt.legend()
plt.grid(True)

plt.show()