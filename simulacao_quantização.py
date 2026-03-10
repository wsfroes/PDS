import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURAÇÕES DO SINAL (MUNDO ANALÓGICO)
# ==========================================
Fs = 1000 
t = np.arange(0, 1, 1/Fs)
frequencia = 2 

sinal_real = np.sin(2 * np.pi * frequencia * t)

# ==========================================
# FUNÇÃO DE QUANTIZAÇÃO
# ==========================================
def quantizar(sinal, bits):
    niveis = 2**bits
    min_val, max_val = np.min(sinal), np.max(sinal)
    sinal_norm = (sinal - min_val) / (max_val - min_val)
    sinal_quantizado = np.round(sinal_norm * (niveis - 1)) / (niveis - 1)
    return sinal_quantizado * (max_val - min_val) + min_val

# Cálculos
bits_falha = 3
sinal_3bits = quantizar(sinal_real, bits_falha)
erro_3bits = sinal_real - sinal_3bits

bits_solucao = 8
sinal_8bits = quantizar(sinal_real, bits_solucao)
erro_8bits = sinal_real - sinal_8bits

# ==========================================
# GERANDO OS GRÁFICOS EM JANELAS SEPARADAS
# ==========================================
# Definindo uma altura maior para os gráficos (10 largura x 6 altura)
tamanho_janela = (10, 6)

# Janela 1: A Falha (3 bits)
plt.figure("Janela 1 - Baixa Resolução (3 bits)", figsize=tamanho_janela)
plt.plot(t, sinal_real, color='lightgray', linestyle='dashed', label='Sinal Real Contínuo')
plt.step(t, sinal_3bits, color='red', where='mid', label='Sinal Digital (3 bits)')
plt.title(f"Print 1: O Desastre da Falta de Resolução ({2**bits_falha} degraus apenas)")
plt.xlim(0, 0.5)
plt.legend(loc='upper right')
plt.grid(True)

# Janela 2: O Ruído de Quantização (3 bits)
plt.figure("Janela 2 - Ruído (3 bits)", figsize=tamanho_janela)
plt.plot(t, erro_3bits, color='darkred')
plt.title("Print 2: O Erro de Quantização (Ruído gerado pelos 3 bits)")
plt.xlim(0, 0.5)
plt.grid(True)

# Janela 3: A Cura (8 bits)
plt.figure("Janela 3 - Alta Resolução (8 bits)", figsize=tamanho_janela)
plt.plot(t, sinal_real, color='lightgray', linestyle='dashed', label='Sinal Real Contínuo')
plt.step(t, sinal_8bits, color='green', where='mid', label='Sinal Digital (8 bits)')
plt.title(f"Print 3: A Cura com Alta Resolução ({2**bits_solucao} degraus)")
plt.xlim(0, 0.5)
plt.legend(loc='upper right')
plt.grid(True)

# Janela 4: O Ruído Mínimo (8 bits)
plt.figure("Janela 4 - Ruído Mínimo (8 bits)", figsize=tamanho_janela)
plt.plot(t, erro_8bits, color='darkgreen')
plt.title("Print 4: O Erro de Quantização com 8 bits (Escala de comparação)")
plt.ylim(np.min(erro_3bits), np.max(erro_3bits)) # Mantém a escala para chocar o aluno
plt.xlim(0, 0.5)
plt.grid(True)

plt.show()