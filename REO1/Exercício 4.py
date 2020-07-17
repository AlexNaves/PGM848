########################################################################################################################
# NOME: ALEX NAVES FERREIRA
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
########################################################################################################################

# Pacotes utilizados
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=2)  # Faz com que os valor tenham duas casas decimais
np.set_printoptions(suppress=True)  # Faz com que os valor tenham duas casas decimais

# EXERCÍCIO 04:

# a) O arquivo dados.txt contem a avaliação de genótipos (primeira coluna) em repetições (segunda coluna)
# quanto a quatro variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy,
# apresente os dados e obtenha as informações de dimensão desta matriz.
print('Letra A:')
dados = np.loadtxt('dados.txt')  # Importando os dados que estão em um arquivo ".txt"
nl, nc = np.shape(dados)
print('Dados: \n{}'.format(dados))
print('Obtendo as dimensão da matriz:')
print('Numero de linhas da matriz: {}'.format(nl))
print('Número de counas da matriz: {}'.format(nc))
print('-' * 100)

# b) Pesquise sobre as funções np.unique e np.where da biblioteca numpy
print('Letra B:')
print('Obtendo informações sobre as funções np.unique e np.where')
print(help(np.unique))  # Mostra o que a função np.unique faz
print('*' * 100)
print(help(np.where))  # Mostra o que a função np.where faz
print('-' * 100)

# c) Obtenha de forma automática os genótipos e quantas repetições foram avaliadas
print('Letra C:')
genotipo = np.unique(dados[:, 0])  # O np.unique vai retornar todos os elementos diferentes possiveis
print('Genótipos avaliados: {}'.format(genotipo))
num = np.unique(dados[:, 1])
print('Foram avaliadas {} repetições'.format(int(max(num))))
print('-' * 100)

# d) Apresente uma matriz contendo somente as colunas 1, 2 e 4
print('Letra D:')
matriz = dados[:, [0, 1, 3]]  # Cria uma matriz conendo todas as linhas ":" das colunas "[0, 1, 3]"
print('Matriz contendo as colunas 1, 2 e 4: \n{}'.format(matriz))
print('Tipo da matriz: {}'.format(type(matriz)))
print('-' * 100)

# e) Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo
# para a variavel da coluna 4. Salve esta matriz em bloco de notas.
print('Letra E:')
mlinha, mcoluna = np.shape(matriz)  # Identificar o número de linhas e colunas da matriz que tem a coluna "4"
print('Número de linhas {} e o número de colunas {}'.format(mlinha, mcoluna))
tor = np.zeros((10, 5))  # Gerando uma nova matriz de zeros com 10 linhas e 4 colunas
print('Matriz de zeros: \n{}'.format(tor))
print('*' * 100)

# matriz[[0, 1, 2], 2] Poderia faze máximo, o mínimo, a média e a variância usando o comando
# porem não e muito eficiente visto que irei repetir a mesma ação varias vez. Neste caso usar um loop "for".


it = 0
for el in np.arange(0, mlinha, 3):  # O "el" irá receber os elementos de 3 em 3, começando do "0" indo ate "mlinha"
    tor[it, 0] = it + 1  # Coloca na coluna "0" os valores dos genotipos
    tor[it, 1] = np.max(matriz[el:el + 3, 2], axis=0)  # Obtem o valor máximo
    # tor vai receber na linha o "it" e na coluna "1" o valor máximo
    # na "matriz" ira pegar as 3 linhas "el:el + 3" da coluna "2" e realizar a operação "np.max"
    tor[it, 2] = np.min(matriz[el:el + 3, 2], axis=0)  # Obtém o valor minimo
    tor[it, 3] = np.mean(matriz[el:el + 3, 2], axis=0)  # Obtém a média
    tor[it, 4] = np.var(matriz[el:el + 3, 2], axis=0)  # Obtém a variância
    it += 1  # Incrementador (it = it +1)


print('Matriz contendo genótipos, máximo, mínimo, média e a variância: \n{}'.format(tor))
# help(np.savetxt)
np.savetxt('Matriz de dados ex3 letra E.txt', tor, fmt='%2.2f', delimiter='\t')  # Savando a matriz em .txt
print('-' * 100)

# f) Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500
# da matriz gerada na letra anterior.
print('Letra F:')
luc = np.where(tor[:, 3] >= 500)
# 1° Selecionando a coluna onde esta as médias "tor[:, 3]"
# 2° Buscar na matriz "tor" em todas as linhas ":" da coluna "3" elementos que atendem a condição "tor[:, 3] >= 500"
# 3° np.where busca a posição destes valores na matriz
cl0 = tor[:, 0]  # 4° Selecionando a coluna onde esta as genotipos "tor[:, 0]"
got = cl0[luc]  # 5° # Acessando os genótipos na "cl0" que tenha as posições da variavel "luc"
# got = tor[:, 0][luc]

print('Os genótipos {} possuem média igual ou superior a 500'.format(got))
print('-' * 100)

# g) Apresente os seguintes graficos:
# Médias dos genótipos para cada variável. Utilizar o comando plt.subplot para mostrar mais de um grafico por figura
print('Letra G:')
nirobi = np.zeros((10, 6))  # Criando uma matriz de zeros com 10 linhas e 6 colunas
h = len(np.unique(dados[:, 0]))

it = 0
for z in np.arange(0, h, 1):
    nirobi[z, 0] = z + 1  # Obtém os genotipos
    nirobi[z, 1] = np.mean((dados[dados[:, 0] == z + 1])[:, 2])  # Obtém a média da variavel 1 (COLUNA 2)
    nirobi[z, 2] = np.mean((dados[dados[:, 0] == z + 1])[:, 3])  # Obtém a média da variavel 2 (COLUNA 3)
    nirobi[z, 3] = np.mean((dados[dados[:, 0] == z + 1])[:, 4])  # Obtém a média da variavel 3 (COLUNA 4)
    nirobi[z, 4] = np.mean((dados[dados[:, 0] == z + 1])[:, 5])  # Obtém a média da variavel 4 (COLUNA 5)
    nirobi[z, 5] = np.mean((dados[dados[:, 0] == z + 1])[:, 6])  # Obtém a média da variavel 5 (COLUNA 6)
    it += 1
print('Médias dos genótipos para cada variável: \n{}'.format(nirobi))

fig = plt.figure('Graficos das médias dos genótipos de cada variável')
plt.subplot(2, 3, 1)  # Criando uma grafico com 6° posições, sendo que este irá ocupar a 1° posição
plt.bar(nirobi[:, 0], nirobi[:, 1], width=0.5, align='center', color='#3d1c02')
plt.title('Variable 1', fontsize=10)
plt.xticks(nirobi[:, 0])
plt.ylabel('Média')

plt.subplot(2, 3, 2)  # Criando uma grafico com 6° posições, sendo que este irá ocupar a 2° posição
plt.bar(nirobi[:, 0], nirobi[:, 2], width=0.5, align='center', color='#be0119')
plt.title('Variable 2', fontsize=10)
plt.xticks(nirobi[:, 0])
plt.ylabel('Média')

plt.subplot(2, 3, 3)  # Criando uma grafico com 6° posições, sendo que este irá ocupar a 3° posição
plt.bar(nirobi[:, 0], nirobi[:, 3], width=0.5, align='center', color='#4a0100')
plt.title('Variable 3', fontsize=10)
plt.xticks(nirobi[:, 0])
plt.ylabel('Média')

plt.subplot(2, 3, 4)  # Criando uma grafico com 6° posições, sendo que este irá ocupar a 4° posição
plt.bar(nirobi[:, 0], nirobi[:, 4], width=0.5, align='center', color='#001146')
plt.title('Variable 4', fontsize=10)
plt.xticks(nirobi[:, 0])
plt.ylabel('Média')

plt.subplot(2, 3, 5)  # Criando uma grafico com 6° posições, sendo que este irá ocupar a 5° posição
plt.bar(nirobi[:, 0], nirobi[:, 5], width=0.5, align='center', color='#8c000f')
plt.title('Variable 5', fontsize=10)
plt.xticks(nirobi[:, 0])
plt.ylabel('Média')
plt.show()
fig.savefig(('Graficos de médias'+'.png'), bbox_inches='tight')
# bbox_inches='tight' ira adequar o tamanho da imagem

# Dispersão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). No eixo X uma variável e no eixo Y outra.
print('Gráficos de Dispersão 2D')
plt.style.use('ggplot')
fig = plt.figure('Dispersão')
plt.subplot(2, 2, 1)   # Criando uma grafico com 4° posições, sendo que este irá ocupar a 1° posição
plt.scatter(nirobi[:, 1], nirobi[:, 2], s=50, alpha=1, c='#380835')  # s=50 (tamanho); alpha=1 (transparencia)
# Coordenada da variavel 1 "nirobi[:, 1]" que ficará no eixo X
# Coordenada da variavel 2 "nirobi[:, 2]" que ficará no eixo Y
plt.title('Dispersão', fontsize=10)
plt.xlabel('Variavel 1')
plt.ylabel('Variavel 2')

plt.subplot(2, 2, 2)   # Criando uma grafico com 4° posições, sendo que este irá ocupar a 2° posição
plt.scatter(nirobi[:, 1], nirobi[:, 3], s=50, alpha=1, c='#070d0d')  # s=50 (tamanho); alpha=1 (transparencia)
# Coordenada da variavel 1 "nirobi[:, 1]" que ficará no eixo X
# Coordenada da variavel 3 "nirobi[:, 3]" que ficará no eixo Y
plt.title('Dispersão', fontsize=10)
plt.xlabel('Variavel 1')
plt.ylabel('Variavel 3')

plt.subplot(2, 2, 3)   # Criando uma grafico com 4° posições, sendo que este irá ocupar a 3° posição
plt.scatter(nirobi[:, 1], nirobi[:, 4], s=50, alpha=1, c='#020035')  # s=50 (tamanho); alpha=1 (transparencia)
# Coordenada da variavel 1 "nirobi[:, 1]" que ficará no eixo X
# Coordenada da variavel 4 "nirobi[:, 4]" que ficará no eixo Y
plt.title('Dispersão', fontsize=10)
plt.xlabel('Variavel 1')
plt.ylabel('Variavel 4')

plt.subplot(2, 2, 4)   # Criando uma grafico com 4° posições, sendo que este irá ocupar a 4° posição
plt.scatter(nirobi[:, 1], nirobi[:, 5], s=50, alpha=1, c='#000000')  # s=50 (tamanho); alpha=1 (transparencia)
# Coordenada da variavel 1 "nirobi[:, 1]" que ficará no eixo X
# Coordenada da variavel 5 "nirobi[:, 5]" que ficará no eixo Y
plt.title('Dispersão', fontsize=10)
plt.xlabel('Variavel 1')
plt.ylabel('Variavel 5')
fig.tight_layout()
plt.show()

fig.savefig(('Graficos de dispersão 2D'+'.png'), bbox_inches='tight')
# bbox_inches='tight' ira adequar o tamanho da imagem
