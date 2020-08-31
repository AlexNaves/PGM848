import cv2  # Importando o pacope opencv
import matplotlib.pyplot as plt

imagem = '101.ge'
imgBGR = cv2.imread(imagem, 1)  # Carregando a imagem colorida

# Convertendo a imagem selecionada nos sistemas
img1 = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)  # Convertendo a imagem recortada de BGR para RBG
img2 = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2Lab)  # Convertendo a imagem recortada de BGR para Lab
img3 = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV)  # Convertendo a imagem recortada de BGR para HSV
img4 = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2YCR_CB)  # Convertendo a imagem recortada de BGR para YCrCb

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
