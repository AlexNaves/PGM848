########################################################################################################################
# NOME: ALEX NAVES FERREIRA
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
########################################################################################################################

# Pacotes utilizados
import numpy as np
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
# Disperão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). No eixo X uma variável e no eixo Y outra.
# Não entendi como se cria um hitograma
