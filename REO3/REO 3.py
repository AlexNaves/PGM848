########################################################################################################################
# NOME: ALEX NAVES FERREIRA
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
########################################################################################################################
# EXERCÍCIO 01

# Importar pacotes
import cv2  # Importando o pacope opencv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from skimage.measure import regionprops
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage

########################################################################################################################
# a) Aplique o filtro de média com cinco diferentes tamanhos de kernel e compare os resultados com a imagem original;
print('Letra A:')

imagem = '104.ge'
imgBGR = cv2.imread(imagem, 1)  # Carregando a imagem colorida
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)  # Convertendo a imagem que esta em BGR para RGB

# Apliando o filtro de medias com diferentes KERNEL
fm1 = cv2.blur(imgRGB, (3, 3))  # Tamanho de kernel (3x3)
fm2 = cv2.blur(imgRGB, (5, 5))  # Tamanho de kernel (5x5)
fm3 = cv2.blur(imgRGB, (7, 7))  # Tamanho de kernel (7x7)
fm4 = cv2.blur(imgRGB, (9, 9))  # Tamanho de kernel (9x9)
fm5 = cv2.blur(imgRGB, (11, 11))  # Tamanho de kernel (11x11)

# Apresentando as imagem n matplotlib
plt.figure('Letra A - Filtro de médias com diferentes kernel')
plt.subplot(2, 3, 1)
plt.imshow(imgRGB)
plt.xticks([])
plt.yticks([])
plt.title('Imagem original', fontsize=10)

plt.subplot(2, 3, 2)
plt.imshow(fm1)
plt.xticks([])
plt.yticks([])
plt.title('Imagem com kernel de 3x3', fontsize=10)

plt.subplot(2, 3, 3)
plt.imshow(fm2)
plt.xticks([])
plt.yticks([])
plt.title('Imagem com kernel de 5x5', fontsize=10)

plt.subplot(2, 3, 4)
plt.imshow(fm3)
plt.xticks([])
plt.yticks([])
plt.title('Imagem com kernel de 7x7', fontsize=10)

plt.subplot(2, 3, 5)
plt.imshow(fm4)
plt.xticks([])
plt.yticks([])
plt.title('Imagem com kernel de 9x9', fontsize=10)

plt.subplot(2, 3, 6)
plt.imshow(fm5)
plt.xticks([])
plt.yticks([])
plt.title('Imagem com kernel de 11x11', fontsize=10)
plt.show()
print('-' * 100)

# b) Aplique diferentes tipos de filtros com pelo menos dois tamanhos de kernel e compare os resultados entre si e
# com a imagem original.
print('Letra B:')

# Filtro de média
m1 = cv2.blur(imgRGB, (9, 9))  # Tamanho de kernel (3x3)
m2 = cv2.blur(imgRGB, (15, 15))  # Tamanho de kernel (5x5)

# Filtro gaussiano - faz uma média podera em reação aos vizinhos, pixels mais proximos tem peso maior
# e pixels mais longe tem peso menor
g1 = cv2.GaussianBlur(imgRGB, (9, 9), 0)
g2 = cv2.GaussianBlur(imgRGB, (15, 15), 0)
# O "0" indica que o peso será determinado automaticamente

# Filtro de mediana
d1 = cv2.medianBlur(imgRGB, 9)
d2 = cv2.medianBlur(imgRGB, 15)

# Filtro bilateral
b1 = cv2.bilateralFilter(imgRGB, 9, 9, 8)
b2 = cv2.bilateralFilter(imgRGB, 15, 15, 13)

# Apresentando as imagens com o matplotlib
plt.figure('Letra B - Diferentes filtros')
plt.subplot(3, 4, 1)
plt.imshow(imgRGB)  # Imagem original em RGB
plt.xticks([])
plt.yticks([])
plt.title('Imagem original', fontsize=10)

plt.subplot(3, 4, 5)
plt.imshow(m1)  # Imagem do filtro de médias com o kernel de (9x9)
plt.xticks([])
plt.yticks([])
plt.title('Filtro de média (9x9)', fontsize=10)

plt.subplot(3, 4, 6)
plt.imshow(m2)  # Imagem do filtro de médias com o kernel de (15x15)
plt.xticks([])
plt.yticks([])
plt.title('Filtro de média (15x15)', fontsize=10)

plt.subplot(3, 4, 7)
plt.imshow(g1)  # Imagem do filtro gaussiano com o kernel de (9x9)
plt.xticks([])
plt.yticks([])
plt.title('Filtro gaussiano (9x9)', fontsize=10)

plt.subplot(3, 4, 8)
plt.imshow(g2)  # Imagem do filtro gaussiano com o kernel de (15x15)
plt.xticks([])
plt.yticks([])
plt.title('Filtro gaussiano (15x15)', fontsize=10)

plt.subplot(3, 4, 9)
plt.imshow(d1)  # Imagem do filtro de mediana com o kernel de (9x9)
plt.xticks([])
plt.yticks([])
plt.title('Filtro de mediana (9x9)', fontsize=10)

plt.subplot(3, 4, 10)
plt.imshow(d2)  # Imagem do filtro de mediana com o kernel de (15x15)
plt.xticks([])
plt.yticks([])
plt.title('Filtro de mediana (15x15)', fontsize=10)

plt.subplot(3, 4, 11)
plt.imshow(b1)  # Imagem do filtro bilateral com o kernel de (9x9)
plt.xticks([])
plt.yticks([])
plt.title('Filtro bilateral (9x9)', fontsize=10)

plt.subplot(3, 4, 12)
plt.imshow(b2)  # Imagem do filtro bilateral com o kernel de (15x15)
plt.xticks([])
plt.yticks([])
plt.title('Filtro bilateral (15x15)', fontsize=10)
plt.show()
print('-' * 100)

# c) Realize a segmentação da imagem utilizando o processo de limiarização. Utilizando o reconhecimento de contornos,
# identifique e salve os objetos de interesse. Além disso, acesse as bibliotecas Opencv e Scikit-Image,
# verifique as variáveis que podem ser mensuradas e extraia as informações pertinentes (crie e salve uma tabela com
# estes dados). Apresente todas as imagens obtidas ao longo deste processo.
print('Letra C:')

# Realizando a segmentação pelo preocesso de limiarização
R, G, B = cv2.split(imgRGB)  # Segmentando o sistema RGB nos 3 canas R, G e B

# Aplicando um filtro no canal R
R = cv2.bilateralFilter(R, 15, 15, 13)

# Histograma da imagem em escala de cinza
histR = cv2.calcHist([R], [0], None, [256], [0, 256])

# Limiarização (Thresholding) da imagem pela técnica de Otsu
(Li, imgOTS) = cv2.threshold(R, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Segmentação da imagem
img_segmentada = cv2.bitwise_and(imgRGB, imgRGB, mask=imgOTS)  # Imagem com os grãos coloridos e o fundo preto

# Utilizando o reconhecimento de contornos
mascara = imgOTS.copy()
cnts, h = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
dimen = []

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    grao = imgOTS[y:y + h, x:x + w]
    obj_rgb = img_segmentada[y:y + h, x:x + w]
    obj_bgr = cv2.cvtColor(obj_rgb, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f's{i + 1}.png', obj_bgr)
    cv2.imwrite(f'sb{i + 1}.png', grao)

    regiao = regionprops(grao)
    print(f'Semente: {i + 1}')
    print(f'Dimensão da Imagem: {np.shape(grao)}')
    print('Medidas Físicas')
    print(f'Centroide: {regiao[0].centroid}')
    print(f'Comprimento do eixo menor: {regiao[0].minor_axis_length}')
    print(f'Comprimento do eixo maior: {regiao[0].major_axis_length}')
    print(f'Razão: {regiao[0].major_axis_length / regiao[0].minor_axis_length}')
    area = cv2.contourArea(c)
    print(f'Área: {area}')
    print(f'Perímetro: {cv2.arcLength(c, True)}')

    print('Medidas de Cor')
    min_val_r, max_val_r, min_loc_r, max_loc_r = cv2.minMaxLoc(obj_rgb[:, :, 0], mask=grao)
    print(f'Valor Mínimo no R: {min_val_r} - Posição: {min_loc_r}')
    print(f'Valor Máximo no R: {max_val_r} - Posição: {max_loc_r}')
    med_val_r = cv2.mean(obj_rgb[:, :, 0], mask=grao)
    print(f'Média no Vermelho: {med_val_r}')

    min_val_g, max_val_g, min_loc_g, max_loc_g = cv2.minMaxLoc(obj_rgb[:, :, 1], mask=grao)
    print(f'Valor Mínimo no G: {min_val_g} - Posição: {min_loc_g}')
    print(f'Valor Máximo no G: {max_val_g} - Posição: {max_loc_g}')
    med_val_g = cv2.mean(obj_rgb[:, :, 1], mask=grao)
    print(f'Média no Verde: ', {med_val_g})

    min_val_b, max_val_b, min_loc_b, max_loc_b = cv2.minMaxLoc(obj_rgb[:, :, 2], mask=grao)
    print(f'Valor Mínimo no B: {min_val_b} - Posição: {min_loc_b}')
    print(f'Valor Máximo no B: {max_val_b} - Posição: {max_loc_b}')
    med_val_b = cv2.mean(obj_rgb[:, :, 2], mask=grao)
    print(f'Média no Azul: ', {med_val_b})
    print('-' * 100)

    # Criando e salvando os dados em uma tabela
    razao = regiao[0].major_axis_length / regiao[0].minor_axis_length
    dimen += [[str(i + 1), str(h), str(w), str(area), str(razao)]]
    dados = pd.DataFrame(dimen)
    dados = dados.rename(columns={0: 'Grãos', 1: 'Altura', 2: 'Largura', 3: 'Area', 4: 'Razão'})
    dados.to_csv('Medidas.csv', index=False)


print(f'Total de sementes: {len(cnts)}')  # Conta o número de grãos

seg = img_segmentada.copy()
cv2.drawContours(seg, cnts, -1, (0, 255, 0), 1)  # Irá circular cada grão com uma linha verde

# Apresentando as imagens
plt.figure('Letra C - Segmentação pela tecnica de OTSU e reconhecimento de contornos')
plt.subplot(1, 3, 1)
plt.imshow(imgOTS, cmap='gray')  # Plota a imagem limiarizada -  Imagem binária
plt.title(f'Imagem binária Otsu (L: {Li})', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(1, 3, 2)
plt.imshow(img_segmentada[:, :, 0], cmap='gray')  # Plota o canal R da imagem segmentada
plt.title('Imagem segmentada (R)', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(1, 3, 3)
plt.imshow(seg, cmap='gray')  # Plota o canal R da imagem segmentada
plt.title('Imagem marcada de verde', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.show()
print('-' * 100)

# d) Utilizando máscaras, apresente o histograma somente dos objetos de interesse.
print('Letra D:')
# Carregando a imagem de interesse
vf = 's82.png'
s82 = cv2.imread(vf, 1)
s82RGB = cv2.cvtColor(s82, cv2.COLOR_BGR2RGB)

im = 'sb82.png'
sb82 = cv2.imread(im, 0)

# Criando os histogramas utilizando mascaras
histR = cv2.calcHist([s82RGB], [0], sb82, [256], [0, 256])
histG = cv2.calcHist([s82RGB], [1], sb82, [256], [0, 256])
histB = cv2.calcHist([s82RGB], [2], sb82, [256], [0, 256])

# Apresentando a imagen do grão colorido
plt.figure('Letra D - Histograma utilizando mascara')
plt.subplot(3, 3, 2)
plt.imshow(s82RGB)  # Imagem do objeto colorida
plt.title('Imagem colorida s82')
plt.xticks([])
plt.yticks([])

# Plotando a imagem do grão em cada canal separadamente
plt.subplot(3, 3, 4)
plt.imshow(s82RGB[:, :, 0], cmap='gray')  # Plotando o canal R
plt.title('Imagem do canal R')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 5)
plt.imshow(s82RGB[:, :, 1], cmap='gray')  # Plotando o canal G
plt.title('Imagem do canal G')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 6)
plt.imshow(s82RGB[:, :, 2], cmap='gray')  # Plotando  canal B
plt.title('Imagem do canal B')
plt.xticks([])
plt.yticks([])

# Plotando o histograma de cada canal separadamente
plt.subplot(3, 3, 7)
plt.plot(histR, color="red")  # Obtendo o histograma do canal R "vermelho"
plt.title("Histograma - R com mascara", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(3, 3, 8)
plt.plot(histG, color="green")  # Obtendo o histograma do canal R "vermelho"
plt.title("Histograma - G com mascara", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(3, 3, 9)
plt.plot(histB, color="blue")  # Obtendo o histograma do canal R "vermelho"
plt.title("Histograma - B com mascara", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)
plt.show()

########################################################################################################################
# Realizando o histograma de cada grão de arroz
"""
IMG_seg = img_segmentada.copy()

for (i, p) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(p)
    IMb = imgOTS[y:y + h, x:x + w]
    obj_rgb = IMG_seg[y:y + h, x:x + w]
    Hist = True

    if Hist:
        # Criando os histogramas de cada canal com a imagem binaria como mascara
        histR = cv2.calcHist([obj_rgb], [0], IMb, [256], [0, 256])
        histG = cv2.calcHist([obj_rgb], [1], IMb, [256], [0, 256])
        histB = cv2.calcHist([obj_rgb], [2], IMb, [256], [0, 256])

        # Apresentando a imagen do grão
        plt.figure('Letra D - Histograma utilizando mascara')
        plt.subplot(3, 3, 2)
        plt.imshow(obj_rgb)  # Imagem do objeto colorida
        plt.title(f'Objeto: {i + 1}')

        # Plotando a imagem do grão em cada canal separadamente
        plt.subplot(3, 3, 4)
        plt.imshow(obj_rgb[:, :, 0], cmap='gray')  # Plotando o canal R
        plt.title(f'Objeto: {i + 1}')

        plt.subplot(3, 3, 5)
        plt.imshow(obj_rgb[:, :, 1], cmap='gray')  # Plotando o canal G
        plt.title(f'Objeto: {i + 1}')

        plt.subplot(3, 3, 6)
        plt.imshow(obj_rgb[:, :, 2], cmap='gray')  # Plotando  canal B
        plt.title(f'Objeto: {i + 1}')

        # Plotando o histograma de cada canal separadamente
        plt.subplot(3, 3, 7)
        plt.plot(histR, color="red")  # Obtendo o histograma do canal R "vermelho"
        plt.title("Histograma - R com mascara", fontsize=10)
        plt.xlim([0, 256])
        plt.xlabel("Valores Pixels", fontsize=10)
        plt.ylabel("Número de Pixels", fontsize=10)

        plt.subplot(3, 3, 8)
        plt.plot(histG, color="green")  # Obtendo o histograma do canal R "vermelho"
        plt.title("Histograma - G com mascara", fontsize=10)
        plt.xlim([0, 256])
        plt.xlabel("Valores Pixels", fontsize=10)
        plt.ylabel("Número de Pixels", fontsize=10)

        plt.subplot(3, 3, 9)
        plt.plot(histB, color="blue")  # Obtendo o histograma do canal R "vermelho"
        plt.title("Histograma - B com mascara", fontsize=10)
        plt.xlim([0, 256])
        plt.xlabel("Valores Pixels", fontsize=10)
        plt.ylabel("Número de Pixels", fontsize=10)
        plt.show()
    else:
        pass
"""
########################################################################################################################
print('-' * 100)

# e) Realize a segmentação da imagem utilizando a técnica de k-means. Apresente as imagens obtidas neste processo.
print('Letra E:')

# Informaçãoes da imagem
print(f'Dimensão: {np.shape(imgRGB)}')
print(f'{np.shape(imgRGB)[0]} x {np.shape(imgRGB)[1]} = {np.shape(imgRGB)[0] * np.shape(imgRGB)[1]}')

# Formatação da imagem para uma matriz de dados
pixel_values = imgRGB.reshape((-1, 3))

# Converção para decimal
pixel_values = np.float32(pixel_values)
print(f'Dimensão Matriz: {pixel_values.shape}')
print('-' * 100)

# K-means
# Critério de Parada
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.5)

k = 2  # Número de Grupos (k)
dist, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
print(f'SQ das Distâncias de Cada Ponto ao Centro: {dist}')
print(f'Dimensão labels: {labels.shape}')
print(f'Valores únicos: {np.unique(labels)}')  # Classidica os pixels de acordo com a sua classe
print(f'Tipo labels: {type(labels)}')
print('-' * 100)

labels = labels.flatten()  # Transformando a labels para um vetor unico
print(f'Dimensão flatten labels: {labels.shape}')
print(f'Tipo labels (f): {type(labels)}')
print('-' * 100)

# Valores dos labels
val_unicos, contagens = np.unique(labels, return_counts=True)
val_unicos = np.reshape(val_unicos, (len(val_unicos), 1))  # Transformando de vetor linha para vetor coluna
contagens = np.reshape(contagens, (len(contagens), 1))  # Transformando de vetor linha para vetor coluna
hist = np.concatenate((val_unicos, contagens), axis=1)
print(f'Histograma: \n {hist}')
print(f'Centroides Decimais: \n {centers}')
print('-' * 100)

# Conversão dos centroides para valores de interos de 8 digitos
centers = np.uint8(centers)
print(f'Centroides uint8: \n {centers}')
print('-' * 100)

# Conversão dos pixels para a cor dos centroides
matriz_segmentada = centers[labels]
print(f'Dimensão Matriz Segmentada: {matriz_segmentada.shape}')
print(f'Matriz Segmentada: \n {matriz_segmentada[0:5, :]}')
print('-' * 100)

# Reformatando a matriz na imagem de formato original
img_segmentada = matriz_segmentada.reshape(imgRGB.shape)

# Grupo 1
original_01 = np.copy(imgRGB)
matriz_or_01 = original_01.reshape((-1, 3))
matriz_or_01[labels != 1] = [0, 0, 0]
img_final_01 = matriz_or_01.reshape(imgRGB.shape)

# Grupo 2
original_02 = np.copy(imgRGB)
matriz_or_02 = original_02.reshape((-1, 3))
matriz_or_02[labels == 1] = [0, 0, 0]
img_final_02 = matriz_or_02.reshape(imgRGB.shape)

# Apresentar Imagem
plt.figure('Letra E - Segmentação pela tecnica de K-MEANS')
plt.subplot(2, 2, 1)
plt.imshow(imgRGB)
plt.title('Imagem original')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(img_segmentada)
plt.title('Rótulos')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(img_final_01)
plt.title('Grupo 1')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(img_final_02)
plt.title('Grupo 2')
plt.xticks([])
plt.yticks([])
plt.show()
print('-' * 100)

# f) Realize a segmentação da imagem utilizando a técnica de watershed. Apresente as imagens obtidas neste processo.
print('Letra F:')
R1, G1, B1 = cv2.split(imgRGB)  # Separando a imagem em 3 canais "R, G e B"
lim, mascara = cv2.threshold(R1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

img_dist = ndimage.distance_transform_edt(mascara)
# Calcula a distancia eucladiana dos pontos brancos da mascara em relação ao fundo

max_local = peak_local_max(img_dist, indices=False, min_distance=25, labels=mascara)
# Retorna uma matriz boleana com a mesma dimensão da imagem mostrando os picos da imagem
print(f'Número de picos: {np.unique(max_local, return_counts=True)}')

marcadores, n_marcadores = ndimage.label(max_local, structure=np.ones((3, 3)))
# Realiza a marcação de cada pico comvalores diferentes
print(f'Análise de conectividade - Marcadores: \n {np.unique(marcadores, return_counts=True)}')

# Reaalizando a segmentação com o WATERSHED
img_ws = watershed(-img_dist, marcadores, mask=mascara)
print(f'Número de grãos: {len(np.unique(img_ws)) - 1}')

# Accessando os grãos individualmente
img_final = np.copy(imgRGB)
img_final[img_ws != 30] = [0, 0, 0]

# Apresentando as imagens
plt.figure('Letra F - Segmentação pela tecnica de WATERSHED')
plt.subplot(2, 3, 1)
plt.imshow(imgRGB)  # Plotando a imagem colorida dos grãos
plt.title('Imagem colorida', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 2)
plt.imshow(R1, cmap='gray')  # Plotando a imagem do canal R
plt.title('R', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 3)
plt.imshow(mascara, cmap='gray')  # Plotando a imagem binaria dos grãos
plt.title('Imagem binaria - Mascara', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 4)
plt.imshow(img_dist, cmap='jet')  # Plotando a distancia dos pontos
plt.title('Distancia', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 5)
plt.imshow(img_ws, cmap='jet')  # Plotando a distancia dos pontos
plt.title('Grãos de arroz', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 6)
plt.imshow(img_final, cmap='jet')  # Plotando a distancia dos pontos
plt.title('Selecionando um unico grão', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.show()
print('-' * 100)

# g) Compare os resultados das três formas de segmentação (limiarização, k-means e watershed) e identifique as
# potencialidades de cada delas.
print('Letra G:')
plt.figure('Letra G - Comparando as três formas de segmentação')
plt.subplot(1, 3, 1)
plt.imshow(img_segmentada)
plt.title('Otsu', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(1, 3, 2)
plt.imshow(img_ws, cmap='jet')
plt.title('Watershed', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(1, 3, 3)
plt.imshow(img_final_01)
plt.title('K-means', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.show()
