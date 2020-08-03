# EXERCÍCIO 01

# Importar pacotes
import cv2  # Importando o pacope opencv
import numpy as np  # Importanto o pacote numpy
import matplotlib.pyplot as plt

########################################################################################################################
# a) Apresente a imagem e as informações de número de linhas e colunas; número de canais e número total de pixels;
print('Letra A:')
# Leitura da imagem
mg = 'arroz.jpeg'  # Nome do arquivo a ser analisado
imgBGR = cv2.imread(mg, 1)  # Carregando a imagem, 0 - Binária e Escala de cinza; 1 - Colorida

# Dados da imagem
print(imgBGR)
lin, col, canais = np.shape(imgBGR)  # Obtém o número de linhas e colunas
print(f'Dimensão da imagem é: {lin} altura x {col} largura')
print(f'Número de canais: {canais}')
print(f'A imagem possui no total {lin * col} pixels')

imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)  # Convertendo a imagem de BGR para RBG. Para imprimir a imagem no
# matplotlib de forma correta. A conversão deve ser feita pois o opencv carrega a imagem colorida em BGR e não em RGB

# Apresentando as imagens original no matplotlib para ver onde recortar
plt.figure('Imagen - Letra A')
plt.imshow(imgRGB)
plt.title('Imagem original')
plt.show()

print('-' * 100)

# b) Faça um recorte da imagem para obter somente a área de interesse. Utilize esta imagem para a solução das
# próximas alternativas;
print('Letra B:')

imgrecorteBGR = imgBGR[109:370, 160:433]  # Recortando a imagem

imgrecorteRGB = cv2.cvtColor(imgrecorteBGR, cv2.COLOR_BGR2RGB)  # Convertendo para plotar a imagem

linR, colR, canaisR = np.shape(imgrecorteBGR)  # Obtém o número de linhas e colunas
print(f'Dimensão da imagem recortada é: {linR} altura x {colR} largura')
print(f'Número de canais da imagem recortada : {canaisR}')
print(f'A imagem recortada possui no total {linR * colR} pixels')

# Apresentando as imagens original e recortada no matplotlib
plt.figure('Imagens - Letra B')
plt.subplot(1, 2, 1)
plt.imshow(imgRGB)
plt.title('Imagem original')

plt.subplot(1, 2, 2)
plt.imshow(imgrecorteRGB)
plt.title('Imagem recortada')
plt.show()
print('-' * 100)

# c) Converta a imagem colorida para uma de escala de cinza (intensidade) e a apresente utilizando os mapas de cores
# “Escala de Cinza” e “JET”;
print('Letra C:')
# Convertenco a imagem colorida e recortada que estava em BGR para escala de cinza
cinza = cv2.cvtColor(imgrecorteBGR, cv2.COLOR_BGR2GRAY)

# Apresentando as imagens no matplotlib
print('Apresentando as imagens no matplotlib em “Escala de Cinza” e “JET”')

plt.figure('Imagens - Letra C')
plt.subplot(1, 2, 1)
plt.imshow(cinza, cmap="gray")  # "gray" delimita entre preto e branco é escala de cinza
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem escala de cinza')
plt.colorbar(orientation='horizontal')  # Coloca uma barra de cores

plt.subplot(1, 2, 2)
plt.imshow(cinza, cmap="jet")  # "jet" delimita do azul ao vermelho
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem JET')
plt.colorbar(orientation='horizontal')  # Coloca uma barra de cores
plt.show()
print('-' * 100)

# d) Apresente a imagem em escala de cinza e o seu respectivo histograma; Relacione o histograma e a imagem.
print('Letra D:')
# Histograma da imagem em escala de cinza
Hcinza = cv2.calcHist([cinza], [0], None, [256], [0, 256])

# Apresentando imagem
plt.figure('Imagens - Letra D')
plt.subplot(1, 2, 1)
plt.imshow(cinza, cmap="gray")  # Plota a imagem em escala de cinza
plt.title('Imagem em escala de cinza')  # Coloca título na imagem

plt.subplot(1, 2, 2)
plt.plot(Hcinza, color="black")  # Plota o histograma da imagem m escala de cinza
plt.title('Histograma')  # Coloca título na imagem
plt.xlabel('Valores pixels')  # Coloca no eixo X os valores dos pixels
plt.ylabel('Número de pixels')  # Coloca no eixo Y o número de pixels

plt.show()
print('-' * 100)

# e) Utilizando a imagem em escala de cinza (intensidade) realize a segmentação da imagem de modo a remover o fundo
# da imagem utilizando um limiar manual e o limiar obtido pela técnica de Otsu. Nesta questão apresente o histograma
# com marcação dos limiares utilizados, a imagem limiarizada (binarizada) e a imagem colorida final obtida
# da segmentação. Explique os resultados.
print('Letra E:')

# Histograma da imagem em escala de cinza
histcinza = cv2.calcHist([cinza], [0], None, [256], [0, 256])

# Limiarização (Thresholding) MANUAL da imagem e escala de cinza
vl = 150  # Valor do limiar
(L, imgLIMIAR) = cv2.threshold(cinza, vl, 255, cv2.THRESH_BINARY)

# Limiarização (Thresholding) da imagem e escala de cinza pela técnica de Otsu
(Lv, imgOTS) = cv2.threshold(cinza, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Segmentação da imagem
img_segmentada = cv2.bitwise_and(imgrecorteRGB, imgrecorteRGB, mask=imgOTS)

# Apresentando as imagens
plt.figure('Limiarização - Letra E')
plt.subplot(3, 3, 1)
plt.imshow(imgrecorteRGB)  # Plota a imagem recortada em RGB
plt.title('Imagem RGB', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 2)
plt.imshow(cinza, cmap="gray")  # Plota a imagem em escala de cinza
plt.title('Imagem em escala de cinza', fontsize=10)
plt.xticks([])
plt.yticks([])

# Imagem limiarizada manualmente e seu histograma
plt.subplot(3, 3, 4)
plt.imshow(imgLIMIAR)  # Plota a imagem limiarizada -  Imagem binária
plt.title(f'Imagem binária (L: {vl}) - Manual', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 5)
plt.plot(histcinza, color="black")  # Plota o histograma da imagem em escala de cinza
plt.axvline(x=vl, color="red")  # Coloca uma linha vermelha no histograma para marcar o limiar
plt.title('Histograma - cinza', fontsize=10)
plt.xlim([0, 256])  # O eixo X vai variar de 0 a 256
plt.xlabel('Valores de pixels', fontsize=10)
plt.ylabel('Número de pixels', fontsize=10)

# Imagem limiarizada pela tecnica de OTSU e seu histograma
plt.subplot(3, 3, 7)
plt.imshow(imgOTS)
plt.title(f'Imagem OTSU (L: {Lv})', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 8)
plt.plot(histcinza, color="black")
plt.axvline(x=Lv, color="red")  # Coloca uma linha vermelha no histograma para marcar o limiar
plt.title('Histograma - OTSU', fontsize=10)
plt.xlim([0, 256])  # O eixo X vai variar de 0 a 256
plt.xlabel('Valores de pixels', fontsize=10)
plt.ylabel('Número de pixels', fontsize=10)

# Segmentação da imagem
plt.subplot(3, 3, 3)
plt.imshow(img_segmentada)
plt.title('Segmentada - RGB')
plt.xticks([])
plt.yticks([])

plt.show()
print('-' * 100)

# f) Apresente uma figura contento a imagem selecionada nos sistemas RGB, Lab, HSV e YCrCb.
print('Letra F:')
# Convertendo a imagem selecionada nos sistemas
img1 = cv2.cvtColor(imgrecorteBGR, cv2.COLOR_BGR2RGB)  # Convertendo a imagem recortada de BGR para RBG
img2 = cv2.cvtColor(imgrecorteBGR, cv2.COLOR_BGR2Lab)  # Convertendo a imagem recortada de BGR para Lab
img3 = cv2.cvtColor(imgrecorteBGR, cv2.COLOR_BGR2HSV)  # Convertendo a imagem recortada de BGR para HSV
img4 = cv2.cvtColor(imgrecorteBGR, cv2.COLOR_BGR2YCrCb)  # Convertendo a imagem recortada de BGR para YCrCb

# Apresentando as imagens no matplotlib
plt.figure('Imagens - Letra F')
plt.subplot(2, 2, 1)
plt.imshow(img1)
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem em RGB')

plt.subplot(2, 2, 2)
plt.imshow(img2)
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem em Lab')

plt.subplot(2, 2, 3)
plt.imshow(img3)
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem em HSV')

plt.subplot(2, 2, 4)
plt.imshow(img4)
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem em YCrCb')
plt.show()
print('-' * 100)

# g) Apresente uma figura para cada um dos sistemas de cores (RGB, HSV, Lab e YCrCb) contendo a imagem de cada um
# dos canais e seus respectivos histogramas.
print('Letra G:')
# Sistema de cor RGB
# Histograma dos canais
hist_r = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([img1], [1], None, [256], [0, 256])
hist_b = cv2.calcHist([img1], [2], None, [256], [0, 256])

# Apresentando as imagens e hitogramas
plt.figure('Sistemas de cores RGB - Letra G')
plt.subplot(2, 4, 1)
plt.imshow(img1)  # Plotando a imagem em RGB
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem RGB', fontsize=10)

plt.subplot(2, 4, 2)
plt.imshow(img1[:, :, 0])  # Obtendo a imagem do canal R "vermelho"
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal R', fontsize=10)

plt.subplot(2, 4, 6)
plt.plot(hist_r, color="red")  # Obtendo o histograma do canal R "vermelho"
plt.title("Histograma - R", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 4, 3)
plt.imshow(img1[:, :, 1])  # Obtendo a imagem do canal G "verde"
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal G', fontsize=10)

plt.subplot(2, 4, 7)
plt.plot(hist_g, color="green")  # Obtendo o histograma do canal G "verde"
plt.title("Histograma - G", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 4, 4)
plt.imshow(img1[:, :, 2])  # Obtendo a imagem do canal B "azul"
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal B', fontsize=10)

plt.subplot(2, 4, 8)
plt.plot(hist_b, color="blue")  # Obtendo o histograma do canal B "azul"
plt.title("Histograma - B", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)
plt.show()

# Sistema de cor HSV
# Histograma dos canais
hist_H = cv2.calcHist([img3], [0], None, [256], [0, 256])
hist_S = cv2.calcHist([img3], [1], None, [256], [0, 256])
hist_V = cv2.calcHist([img3], [2], None, [256], [0, 256])

# Apresentando as imagens e hitogramas
plt.figure('Sistemas de cores HSV - Letra G')
plt.subplot(2, 4, 1)
plt.imshow(img3)  # Plotando a imagem em HSV
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem HSV', fontsize=10)

plt.subplot(2, 4, 2)
plt.imshow(img3[:, :, 0])  # Obtendo a imagem do canal H
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal H', fontsize=10)

plt.subplot(2, 4, 6)
plt.plot(hist_H, color="black")  # Obtendo o histograma do canal H
plt.title("Histograma - H", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 4, 3)
plt.imshow(img3[:, :, 1])  # Obtendo a imagem do canal S
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal S', fontsize=10)

plt.subplot(2, 4, 7)
plt.plot(hist_S, color="black")  # Obtendo o histograma do canal S
plt.title("Histograma - S", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 4, 4)
plt.imshow(img3[:, :, 2])  # Obtendo a imagem do canal V
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal V', fontsize=10)

plt.subplot(2, 4, 8)
plt.plot(hist_V, color="black")  # Obtendo o histograma do canal V
plt.title("Histograma - V", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)
plt.show()

# Sistema de cor Lab
# Histograma dos canais
hist_L = cv2.calcHist([img2], [0], None, [256], [0, 256])
hist_A = cv2.calcHist([img2], [1], None, [256], [0, 256])
hist_B = cv2.calcHist([img2], [2], None, [256], [0, 256])

# Apresentando as imagens e hitogramas
plt.figure('Sistemas de cores Lab - Letra G')
plt.subplot(2, 4, 1)
plt.imshow(img2)  # Plotando a imagem em Lab
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem Lab', fontsize=10)

plt.subplot(2, 4, 2)
plt.imshow(img2[:, :, 0])  # Obtendo a imagem do canal L
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal L', fontsize=10)

plt.subplot(2, 4, 6)
plt.plot(hist_L, color="black")  # Obtendo o histograma do canal L
plt.title("Histograma - L", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 4, 3)
plt.imshow(img2[:, :, 1])  # Obtendo a imagem do canal a
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal a', fontsize=10)

plt.subplot(2, 4, 7)
plt.plot(hist_A, color="black")  # Obtendo o histograma do canal a
plt.title("Histograma - a", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 4, 4)
plt.imshow(img2[:, :, 2])  # Obtendo a imagem do canal b
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal b', fontsize=10)

plt.subplot(2, 4, 8)
plt.plot(hist_B, color="black")  # Obtendo o histograma do canal b
plt.title("Histograma - b", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)
plt.show()

# Sistema de cor YCrCb
# Histograma dos canais
hist_Y = cv2.calcHist([img4], [0], None, [256], [0, 256])
hist_Cr = cv2.calcHist([img4], [1], None, [256], [0, 256])
hist_Cb = cv2.calcHist([img4], [2], None, [256], [0, 256])

# Apresentando as imagens e hitogramas
plt.figure('Sistemas de cores YCrCb - Letra G')
plt.subplot(2, 4, 1)
plt.imshow(img4)  # Plotando a imagem em YCrCb
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Imagem YCrCb', fontsize=10)

plt.subplot(2, 4, 2)
plt.imshow(img4[:, :, 0])  # Obtendo a imagem do canal Y
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal Y', fontsize=10)

plt.subplot(2, 4, 6)
plt.plot(hist_Y, color="black")  # Obtendo o histograma do canal Y
plt.title("Histograma - Y", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 4, 3)
plt.imshow(img4[:, :, 1])  # Obtendo a imagem do canal Cr
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal Cr', fontsize=10)

plt.subplot(2, 4, 7)
plt.plot(hist_Cr, color="black")  # Obtendo o histograma do canal Cr
plt.title("Histograma - Cr", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 4, 4)
plt.imshow(img4[:, :, 2])  # Obtendo a imagem do canal Cb
plt.xticks([])  # Eliminar o eixo X
plt.yticks([])  # Eliminar o eixo Y
plt.title('Canal Cb', fontsize=10)

plt.subplot(2, 4, 8)
plt.plot(hist_Cb, color="black")  # Obtendo o histograma do canal Cb
plt.title("Histograma - Cb", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)
plt.show()
print('-' * 100)

# h) Encontre o sistema de cor e o respectivo canal que propicie melhor segmentação da imagem de modo a remover o fundo
# da imagem utilizando limiar manual e limiar obtido pela técnica de Otsu. Nesta questão apresente o histograma com
# marcação dos limiares utilizados, a imagem limiarizada (binarizada) e a imagem colorida final obtida da segmentação.
# Explique os resultados e sua escolha pelo sistema de cor e canal utilizado na segmentação. Nesta questão apresente a
# imagem limiarizada (binarizada) e a imagem colorida final obtida da segmentação.
print('Letra H:')

EX = cv2.cvtColor(imgrecorteBGR, cv2.COLOR_BGR2RGB)
R, G, B = cv2.split(EX)  # Separando os 3 canas do sistema RGB

# CANAL R
# Histograma
hisR = cv2.calcHist([R], [0], None, [256], [0, 256])

# Limiarização (Thresholding) MANUAL de um canal do sistema RGB
limiar_R = 120
(L_R, img_limiar_R) = cv2.threshold(R, limiar_R, 255, cv2.THRESH_BINARY)

# Limiarização (Thresholding) de um canal do sistema RGB pela técnica de Otsu
(LoR, OTlimiar_R) = cv2.threshold(R, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Segmentação da imagem
imgSegR = cv2.bitwise_and(EX, EX, mask=OTlimiar_R)

# Apresentando as imagens e os histgramas para o canal R
# Imagem limiarizada manualmente e seu histograma
plt.figure('Imagens do canal R - Letra H')
plt.subplot(2, 3, 1)
plt.imshow(img_limiar_R)  # Plota a imagem limiarizada -  Imagem binária
plt.title(f'Imagem binária (L: {L_R}) - Manual', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 4)
plt.plot(hisR, color="black")  # Plota o histograma do canal R
plt.axvline(x=L_R, color="red")  # Coloca uma linha vermelha no histograma para marcar o limiar
plt.title('Histograma - canal R MANUAL', fontsize=10)
plt.xlim([0, 256])  # O eixo X vai variar de 0 a 256
plt.xlabel('Valores de pixels', fontsize=10)
plt.ylabel('Número de pixels', fontsize=10)

# Imagem limiarizada pela tecnica de Otsu e seu histograma para o canal R
plt.subplot(2, 3, 2)
plt.imshow(OTlimiar_R)  # Plota a imagem limiarizada -  Imagem binária
plt.title(f'Imagem binária (L: {LoR}) - Otsu', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 5)
plt.plot(hisR, color="black")
plt.axvline(x=LoR, color="red")  # Coloca uma linha vermelha no histograma para marcar o limiar
plt.title('Histograma - canal R OTSU', fontsize=10)
plt.xlim([0, 256])  # O eixo X vai variar de 0 a 256
plt.xlabel('Valores de pixels', fontsize=10)
plt.ylabel('Número de pixels', fontsize=10)

# Segmentação para o canal R
plt.subplot(2, 3, 3)
plt.imshow(imgSegR)  # Plota a imagem segmentada
plt.title('Imagem segmentada - RGB', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.show()

# CANAL G
# Histograma
hisG = cv2.calcHist([G], [0], None, [256], [0, 256])

# Limiarização (Thresholding) MANUAL de um canal do sistema RGB
limiar_G = 140
(L_G, img_limiar_G) = cv2.threshold(G, limiar_G, 255, cv2.THRESH_BINARY)

# Limiarização (Thresholding) de um canal do sistema RGB pela técnica de Otsu
(LoG, OTlimiar_G) = cv2.threshold(G, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Segmentação da imagem
imgSegG = cv2.bitwise_and(EX, EX, mask=OTlimiar_G)

# Apresentando as imagens e os histgramas para o canal G
# Imagem limiarizada manualmente e seu histograma
plt.figure('Imagens do canal G - Letra H')
plt.subplot(2, 3, 1)
plt.imshow(img_limiar_G)  # Plota a imagem limiarizada -  Imagem binária
plt.title(f'Imagem binária (L: {L_G}) - Manual', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 4)
plt.plot(hisG, color="black")  # Plota o histograma do canal Y
plt.axvline(x=L_G, color="red")  # Coloca uma linha vermelha no histograma para marcar o limiar
plt.title('Histograma - canal G MANUAL', fontsize=10)
plt.xlim([0, 256])  # O eixo X vai variar de 0 a 256
plt.xlabel('Valores de pixels', fontsize=10)
plt.ylabel('Número de pixels', fontsize=10)

# Imagem limiarizada pela tecnica de Otsu e seu histograma para o canal G
plt.subplot(2, 3, 2)
plt.imshow(OTlimiar_G)  # Plota a imagem limiarizada -  Imagem binária
plt.title(f'Imagem binária (L: {LoG}) - Otsu', fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 5)
plt.plot(hisG, color="black")
plt.axvline(x=LoG, color="red")  # Coloca uma linha vermelha no histograma para marcar o limiar
plt.title('Histograma - canal G OTSU', fontsize=10)
plt.xlim([0, 256])  # O eixo X vai variar de 0 a 256
plt.xlabel('Valores de pixels', fontsize=10)
plt.ylabel('Número de pixels', fontsize=10)

# Segmentação para o canal G
plt.subplot(2, 3, 3)
plt.imshow(imgSegG)  # Plota a imagem segmentada
plt.title('Imagem segmentada - RGB', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.show()
print('-' * 100)

# i) Obtenha o histograma de cada um dos canais da imagem em RGB, utilizando como mascara a imagem limiarizada
# (binarizada) da letra h.
print('Letra I:')
# Histograma dos canais RGB
histR = cv2.calcHist([imgSegR], [0], OTlimiar_R, [256], [0, 256])
histG = cv2.calcHist([imgSegR], [1], OTlimiar_R, [256], [0, 256])
histB = cv2.calcHist([imgSegR], [2], OTlimiar_R, [256], [0, 256])

# Apresentando as imagens e os hitogramas dos canais RGB
plt.figure('Histogramas dos canais RGB com mascara - Letra I')
plt.subplot(2, 3, 1)
plt.plot(histR, color="red")  # Obtendo o histograma do canal R "vermelho"
plt.title("Histograma - R com mascara", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 3, 4)
plt.imshow(imgSegR[:, :, 0])  # Obtendo a imagem do canal R "vermelho"
plt.title("R", fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 2)
plt.plot(histG, color="green")  # Obtendo o histograma do canal G "verde"
plt.title("Histograma - G com mascara", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 3, 5)
plt.imshow(imgSegR[:, :, 1])  # Obtendo a imagem do canal G "verde"
plt.title("G", fontsize=10)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 3)
plt.plot(histB, color="blue")  # Obtendo o histograma do canal B "azul"
plt.title("Histograma - B com mascara", fontsize=10)
plt.xlim([0, 256])
plt.xlabel("Valores Pixels", fontsize=10)
plt.ylabel("Número de Pixels", fontsize=10)

plt.subplot(2, 3, 6)
plt.imshow(imgSegR[:, :, 2])  # Obtendo a imagem do canal B "azul"
plt.title("B", fontsize=10)
plt.xticks([])
plt.yticks([])
plt.show()
print('-' * 100)

# j) Realize operações aritméticas na imagem em RGB de modo a realçar os aspectos de seu interesse. Exemplo (2*R-0.5*G).
# Explique a sua escolha pelas operações aritméticas. Segue abaixo algumas sugestões.
print('Letra J:')
# Operações nos canais da imagem
imgOPR1 = 1.7 * imgRGB[:, :, 0] - 1.2 * imgRGB[:, :, 1]

# Converção da variavel para inteiro de 8 bits
imgOPR = imgOPR1.astype(np.uint8)

# Histograma
histw = cv2.calcHist([imgOPR], [0], None, [256], [0, 256])

# Limiarização de Otsu
(M, img_OTSU) = cv2.threshold(imgOPR, 0, 256, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Segmentação da imagem com mascara
img_SEGM = cv2.bitwise_and(imgRGB, imgRGB, mask=img_OTSU)

# Apresentando a imagem
plt.figure('Imagens Operações - Letra J')
plt.subplot(2, 3, 1)
plt.imshow(imgRGB, cmap='gray')
plt.title('RGB')

plt.subplot(2, 3, 2)
plt.imshow(imgOPR, cmap='gray')
plt.title('1.7*B - 1,2*G')

plt.subplot(2, 3, 3)
plt.plot(histw, color='black')
# plt.axline(x=M, color='black')
plt.xlim([0, 256])
plt.xlabel('Valores de pixels')
plt.ylabel('Número de pixels')

plt.subplot(2, 3, 4)
plt.imshow(img_OTSU, cmap='gray')
plt.title('Imagem binária')

plt.subplot(2, 3, 5)
plt.imshow(img_SEGM, cmap='gray')
plt.title('Imagem segmentada com mascara')
plt.xticks([])
plt.yticks([])

plt.show()
