########################################################################################################################
# NOME: ALEX NAVES FERREIRA
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
########################################################################################################################

# Pacotes utilizados
import numpy as np
import matplotlib.pyplot as plt
import math
np.set_printoptions(precision=2)  # Faz com que os valor tenham duas casas decimais
np.set_printoptions(suppress=True)  # Faz com que os valor tenham duas casas decimais

# EXERCÍCIO 03:

# a) Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral de
# um vetor qualquer, baseada em um loop (for).
print('Letra A:')
from funcao_med_var import media, variancia
print('-' * 100)

# b) Simule três arrays com a biblioteca numpy de 10, 100, e 1000 valores e com distribuição normal com média 100
# e variância 2500. Pesquise na documentação do numpy por funções de simulação.
print('Letra B:')
# Distribuição normal np.random.normal(mu, sigma, size): "mu" = média; "sigma" = desvio padrão; size = tamanho
desvio = math.sqrt(2500)  # O math.sqrt vai tirar a raiz da variância obtendo assim o desvio
print('Desvio: {}'.format(desvio))

simulacao1 = np.random.normal(100, math.sqrt(2500), 10)
simulacao2 = np.random.normal(100, math.sqrt(2500), 100)
simulacao3 = np.random.normal(100, math.sqrt(2500), 1000)
simulacao4 = np.random.normal(100, math.sqrt(2500), 100000)

print('Simulação 1 com tamanho 10: \n{}'.format(simulacao1))
print('*' * 100)
print('Simulação 2 com tamanho 100: \n{}'.format(simulacao2))
print('*' * 100)
print('Simulação 3 com tamanho 1000: \n{}'.format(simulacao3))
print('*' * 100)
print('Simulação 4 com tamanho 100000: \n{}'.format(simulacao4))
print('-' * 100)

# c) Utilize a função criada na letra a para obter as médias e variâncias dos vetores simulados na letra b.
print('Letra C:')
print('A simulação 1 tem média {:.3f} e variância {:.3f}'.format(media(simulacao1), variancia(simulacao1)))
print('A simulação 2 tem média {:.3f} e variância {:.3f}'.format(media(simulacao2), variancia(simulacao2)))
print('A simulação 3 tem média {:.3f} e variância {:.3f}'.format(media(simulacao3), variancia(simulacao3)))
print('A simulação 4 tem média {:.3f} e variância {:.3f}'.format(media(simulacao4), variancia(simulacao4)))
print('-' * 100)

# d) Crie histogramas com a biblioteca matplotlib dos vetores simulados com valores de 10, 100, 1000 e 100000.
print('Letra D:')
fig, axes = plt.subplots(nrows=2, ncols=2)  # Criando uma figura com 4 posições (2 linhas e 2 colunas)
ax1, ax2, ax3, ax4 = axes.flatten()  # Ordem em que os graficos serão colocados,
# sem a utilização do plt.subplot() para cada dos graficos

ax1.hist(simulacao1, color='darkcyan')
ax1.set_title('Histograma, $\mu=100$, $\sigma=50$, n = 10', fontsize=10)

ax2.hist(simulacao2, color='darkviolet')
ax2.set_title('n = 100', fontsize=10)

ax3.hist(simulacao3, color='forestgreen')
ax3.set_title('n = 1000', fontsize=10)

ax4.hist(simulacao4, color='slategray')
ax4.set_title('n = 100000', fontsize=10)

fig.tight_layout()  # tight_layout sera aplicado sobre a "Figura" criada
plt.show()  # Imprime o grafico na tela
