########################################################################################################################
# NOME: ALEX NAVES FERREIRA
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
########################################################################################################################

# Pacotes utilizados
import numpy as np
# import matplotlib.pyplot as plt
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
desvio = int(np.sqrt(2500))  # Desvio é a raiz da variância
print('Desvio: {}'.format(desvio))

simulacao1 = np.random.normal(100, desvio, 10)
simulacao2 = np.random.normal(100, desvio, 100)
simulacao3 = np.random.normal(100, desvio, 1000)
simulacao4 = np.random.normal(100, desvio, 100000)
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
# Não entendi como se cria o histograma
"""
plt.figure('Grafico de barras')
plt.subplot(2, 2, 1)
plt.bar(simulacao1)
plt.title('Simulação 1 - 10')
plt.show()

plt.figure('Grafico de barras')
plt.subplot(2, 2, 2)
plt.bar(simulacao2)
plt.title('Simulação 1 - 100')
plt.show()

plt.figure('Grafico de barras')
plt.subplot(2, 2, 3)
plt.bar(simulacao3)
plt.title('Simulação 1 - 1000')
plt.show()

plt.figure('Grafico de barras')
plt.subplot(2, 2, 4)
plt.bar(simulacao4)
plt.title('Simulação 1 - 100000')
plt.show()
"""

