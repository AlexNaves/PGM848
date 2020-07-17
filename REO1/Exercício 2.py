########################################################################################################################
# NOME: ALEX NAVES FERREIRA
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
########################################################################################################################

# Exercício 02

# Pacotes utilizados
import numpy as np

# a) Declare a matriz abaixo com a biblioteca numpy.
# 1 3 22
# 2 8 18
# 3 4 22
# 4 1 23
# 5 2 52
# 6 2 18
# 7 2 25

print('Letra A:')
matriz = np.array([[1, 3, 22],  # Declarando uma matriz
                   [2, 8, 18],
                   [3, 4, 22],
                   [4, 1, 23],
                   [5, 2, 52],
                   [6, 2, 18],
                   [7, 2, 25]])
print('Matriz: \n{}'.format(matriz))
print('-' * 100)

# b) Obtenha o número de linhas e de colunas desta matriz
print('Letra B:')
nl, nc = np.shape(matriz)  # Obtendo as dimensões da matriz
print('Número de linhas da matriz: {}'.format(nl))
print('Número de colunas da matriz: {}'.format(nc))
print('-' * 100)

# c) Obtenha as médias das colunas 2 e 3.
print('Letra C:')
print('Matriz: \n{}'.format(matriz))
mediac2 = np.mean(matriz[:, 2])  # Obtendo a media da coluna 2
mediac3 = np.mean(matriz[:, -1])  # Obtendo a media da coluna 2, o -1 refere-se a ultima coluna da matriz
print('A média da coluna 2 é {:.3f} e da coluna 3 é {:.3f}'.format(mediac2, mediac3))
print('-' * 100)

# d) Obtenha as médias das linhas considerando somente as colunas 2 e 3
print('Letra D:')
print('Matriz: \n{}'.format(matriz))
print('Na linha 1 a média é: {}'.format(sum(matriz[0, [1, 2]])/2))
print('Na linha 2 a média é: {}'.format(sum(matriz[1, [1, 2]])/2))
print('Na linha 3 a média é: {}'.format(sum(matriz[2, [1, 2]])/2))
print('Na linha 4 a média é: {}'.format(sum(matriz[3, [1, 2]])/2))
print('Na linha 5 a média é: {}'.format(sum(matriz[4, [1, 2]])/2))
print('Na linha 6 a média é: {}'.format(sum(matriz[5, [1, 2]])/2))
print('Na linha 7 a média é: {}'.format(sum(matriz[6, [1, 2]])/2))
print('-' * 100)

# e) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença
# e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade inferior a 5.
print('Letra E:')
print('Matriz: \n{}'.format(matriz))
col1 = matriz[:, 1]  # Selecionando a coluna de severidade (segunda coluna - posição 1)
nota = np.where(col1 < 5)  # Acessando a posição das notas de severidade na "col1" que atende a condição "col1 < 5"
col0 = matriz[:, 0]  # Selecionando a coluna de genótipos (primeira coluna - posição 0)
genotipon = col0[nota]  # Acessando os genótipos na "col0" que tenha as posições da variavel "nota"
print('A posição das notas de severidade na coluna 2 inferior a 5 é: {}'.format(nota[0]))
print('Os genótipos que tem nota de severidade inferior a 5 são: {}'.format(genotipon))
print('-' * 100)

# f) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e
# e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou igual a 22.
print('Letra F:')
print('Matriz: \n{}'.format(matriz))
col2 = matriz[:, 2]  # Selecionando a coluna de peso (terceira coluna - posição 2)
peso = np.where(col2 >= 22)  # Acessando a posição dos pesos na "col2" que atende a condição "col2 >= 22"
print('A posição dos pesos na coluna 3 superior ou igual a 22 é: {}'.format(peso[0]))
col0 = matriz[:, 0]  # Selecionando a coluna de genótipos (primeira coluna - posição 0)
genotipop = col0[peso]  # Acessando os genótipos na "col0" que tenha as posições da variavel "peso"
print('Os genótipos que tem peso de 100 grãos superior ou igual a 22 são: {}'.format(genotipop))
print('-' * 100)

# g) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença
# e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3
# e peso de 100 grãos igual ou superior a 22.
print('Letra G:')
print('Matriz: \n{}'.format(matriz))
c1 = matriz[:, 1]  # Selecionando a coluna de severidade (segunda coluna - posição 1)
c2 = matriz[:, 2]  # Selecionando a coluna de peso (terceira coluna - posição 2)
c0 = matriz[:, 0]  # Selecionando a coluna de genótipos (primeira coluna - posição 0)
dados = np.where((c1 <= 3) & (c2 >= 22))  # Acessando a posição dos génotipos que atendem as condições
gen = c0[(c1 <= 3) & (c2 >= 22)]  # Acessando os genótipos na "col0" que atende as condições "(c1 <= 3) & (c2 >= 22)"
print('Os genótipos com nota igual ou inferior a 3 e peso igual ou superior a 22 são: {}'.format(gen))
print('A posição dos genótipos com nota igual ou inferior a 3 e peso igual ou superior a 22 são: {}'.format(dados[0]))
print('-' * 100)

# h) Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz
# e o seu respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido.
# Apresente a seguinte mensagem a cada iteração "Na linha X e na coluna Y ocorre o valor: Z".
# Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25
print('Letra H:')
print('Matriz: \n{}'.format(matriz))
contador = 0
for i in np.arange(0, nl, 1):
    for j in np.arange(0, nc, 1):
        contador += 1
        print('Iteração: {}'.format(contador))
        print('Na linha {} e na coluna {} ocorre o valor: {}'.format(i, j, matriz[i, j]))
g25 = col0[col2 >= 25]  # Acessando os genótipos que atenda a condição de que na coluna 2 tenham valores ">= 25"
print('Os genótipos com peso de 100 grãos igual ou superior a 25 são: {}'.format(g25))
print('-' * 100)
