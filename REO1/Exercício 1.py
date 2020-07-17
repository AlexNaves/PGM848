########################################################################################################################
# NOME: ALEX NAVES FERREIRA
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
########################################################################################################################

# Pacotes utilizados
import numpy as np  # Importando a bibliotca Numpy

np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

# EXERCÍCIO 01:

# a) Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy.
print('Letra A:')
v1 = np.array([43.5, 150.30, 17, 28, 35, 79, 20, 99.07, 15])  # Declarando um vetor
print('Vetor 1: {}'.format(v1))
print('Dimensão do vetor(v1): {}'.format(len(v1)))  # Solicitando a dimenção do vetor
print('-' * 100)

# b) Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.
print('Letra B:')
dimensao = len(v1)  # Solicitando a dimenção do vetor
media = np.mean(v1)  # Solicitando a média do vetor
maximo = np.max(v1)  # Acessando o maior valor dentro do vetor
minimo = np.min(v1)  # Acessando o menor valor dentro do vetor
variancia = np.var(v1)  # Solicitando a variancia do veto
print('O vetor possui {} caracteres.'.format(dimensao))
print('A média é: {:.3f}'.format(media))
print('O máximo é: {}'.format(maximo))
print('O minimo é: {}'.format(minimo))
print('A variância é: {:.3f}'.format(variancia))
print('-' * 100)

# c) Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor declarado
# na letra a e o valor da média deste.
print('Letra C:')
vnew = (v1 - media) ** 2  # Diferença entre os elemtos do vetor e a media "(v1 - media)" elevados ao quadrado "**2"
print('Valor de cada elemento do vetor original (v1) menos a média elevado ao quedrado: \n{}'.format(vnew))
print('-' * 100)

# d) Obtenha um novo vetor que contenha todos os valores superiores a 30.
print('Letra D:')
print('Vetor original: {}'.format(v1))
v30 = v1 > 30  # Acessando os valores no vetor "v1" que atende a condição "v1 > 30"
print('Vetor com os valores superior a 30: {}'.format(v30))  # Retorna True (valor maior) ou False (valor menor)
vetor30 = v1[v30]  # Ira pegar dentro do vetor "v1" valores que se enquadre na condição da variavel "v30" -> "v1 > 30"
print('Vetor com os valores superior a 30: {}'.format(vetor30))
print('-' * 100)

# e) Identifique quais as posições do vetor original possuem valores superiores a 30
print('Letra E:')
print('Vetor original: {}'.format(v1))
posv30 = np.where(v1 > 30)  # Identifica a posição no vetor "v1" que se enquadra na condição "v1 > 30"
# O np.where retorna uma lista e o elemento da posição "0" é o que contém a posição dos valores
print('Posição dos valores superiores a 30: {}'.format(posv30[0]))
print('-' * 100)

# f) Apresente um vetor que contenha os valores da primeira, quinta e última posição.
print('Letra F:')
print('Vetor original: {}'.format(v1))
vomega = v1[[0, 4, -1]]  # Pega os valores das posições "0, 4 e -1" o -1 e o ultimo elemento do vetor
print('Vetor que contém os valores da 1°, 5° e 8° posição: {}'.format(vomega))
print('-' * 100)

# g) Crie uma estrutura de repetição usando o for para apresentar cada valor e
# a sua respectiva posição durante as iterações
print('Letra G:')
print('Vetor original: {}'.format(v1))
it = 0
# O "i" é a variavel que vai receber o "ranger"
for i in range(0, dimensao, 1):  # 0 é o primeiro valor, dimensao é o ultimo valor, 1 e de quanto em quanto irá aumentar
    it = it + 1
    print('Iterações: {}'.format(it))
    print('Na posição {} há o elemento {}'.format(i, v1[int(i)]))
    print('-' * 100)
print('-' * 100)

# h) Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.
print('Letra H:')
somaq = 0
for el in v1:  # "el" irá receber um elemento do vetor a cada loop do "for" elevar ao quadrador
    # e somar com o proximo valor elevado ao quadrado
    somaq = somaq + (el ** 2)
print('Soma dos quadrados de cada valor do vetor: {:.3f}'.format(somaq))
print('-' * 100)

# i) Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor
print('Letra I:')

it = 0
while v1[it] != (len(v1)):  # Enquanto o it for diferente da dimensão do vetor o "WHILE" irá rodar
    # Quando o it for igual dimensão do vetor o "WHILE" vai parar de rodar
    print('O valor que esta na posição {} do vetor é {}.'.format(it, v1[it]))
    it = it + 1
    # Colocando outra condição a função WHILE
    if it == (len(v1)):  # Quando o it tiver a mesma quantidade de elementos que o vetor (v1) o "WHILE" irá parar
        break
print('-' * 100)

# j) Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.
print('Letra J:')
seq = range(1, 10, 1)  # Irá gera a sequência que não da para ver
print('Sequência: {}'.format(seq))
print('O tipo da variavel é: {}'.format(type(seq)))
listaseq = list(seq)  # Para acessar os valores deve se transformar a sequência em lista
print('Lista da sequência gerada: {}'.format(listaseq))
print('O tipo da sequência transformada é: {}'.format(type(listaseq)))
print('Dimensão da sequência: {}'.format(len(listaseq)))
print('-' * 100)

# k) Concatene o vetor da letra a com o vetor da letra j.
print('Letra K:')
print('Vetor letra A: {}'.format(v1))
print('Vetor letra J: {}'.format(listaseq))
vetoresconcatenados = np.concatenate((v1, listaseq), axis=0)
print('Vetores da letra A e J concatenados: \n{}'.format(vetoresconcatenados))
print('-' * 100)
