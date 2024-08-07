# **Exercício: Teste z para Altura Média da Turma**

# Cenário:

# Queremos avaliar se a altura média da turma on35 é significativamente diferente da altura média nacional da população feminina brasileira, que é de 161 cm. 

# Objetivo:

#     Verificar se a altura média da turma é significativamente diferente de 161 cm.


# Dados da Amostra: até o momento:
#     Altura da turma (em cm): [165, 157, 163, 170, 167, 161, 160, 170, 157, 160, 157, 168, 162, 170, 167, 165, 
# 166, 158, 174, 169, 158, 174, 169, 163, 174, 162, 170, 155, 154, 158, 160, 166]

# H0 = Supõe que não há diferença entre a média da amostra e a média da população (161 cm). 
#      A altura média da turma é 161 cm
# H1 = Supõe que que há uma diferença entre a média da amostra e a média da população. 
#      A altura média da turma é diferente de 161 cm

# Perguntas:

# Calcule a estatística *z* e o valor *p* para verificar se a altura média da turma é significativamente diferente de 161 cm.

import numpy as np
from statsmodels.stats.weightstats import ztest
import matplotlib.pyplot as plt
from scipy.stats import norm

# Dados da amostra
altura_turma = np.array([165, 157, 163, 170, 167, 161, 160, 170, 157, 160, 157, 168, 162, 170, 167, 165, 166, 158, 174, 169, 158, 174, 169, 163, 174, 162, 170, 155, 154, 158, 160, 166])
media_nacional = 161
alfa = 0.05

# Teste z para uma amostra
z_statistic, p_value = ztest(altura_turma, value=media_nacional)
print("Teste z para uma amostra:")
print(f"z-statistic: {z_statistic:.4f}, p-value: {p_value:.4f}")

# Interprete os resultados: Preciso saber se rejeitou ou não a hipótese nula.
if p_value < alfa:
    print("Rejeitamos a hipótese nula. Há evidências de que a altura média da turma é diferente de 161 cm.")
else:
    print("Não rejeitamos a hipótese nula. Não há evidências de que a altura média da turma é diferente de 161 cm.")

# Parâmetros da distribuição normal padrão
mu = 0
sigma = 1

# Valores do eixo x
x = np.linspace(-4, 4, 1000)

# Função densidade de probabilidade (PDF) da distribuição normal padrão
pdf = norm.pdf(x, mu, sigma)

# Z score que queremos destacar
z_score = round(z_statistic,4)

# Gerar o gráfico
plt.figure(figsize=(7, 5))

# Plotar a distribuição normal padrão
plt.plot(x, pdf, label='Distribuição Normal Padrão')

# Destacar o Z score
plt.fill_between(x, 0, pdf, where=(x >= z_score), color='red', alpha=0.5, label=f'Z score = {z_score}')
plt.axvline(z_score, color='red', linestyle='--')

# Adicionar títulos e legendas
plt.title('Distribuição Normal Padrão com Z score Destacado')
plt.xlabel('Z score')
plt.ylabel('Densidade de Probabilidade')
plt.legend()

# Um Z score de 2.9591 indica que estura média das meninas da turma é maior do que a estatura da população em geral(161 cm).

# Mostrar o gráfico
plt.show()
