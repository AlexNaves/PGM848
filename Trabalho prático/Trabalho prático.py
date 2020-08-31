# Importar pacotes
import cv2  # Importando o pacope opencv
import numpy as np
import pandas as pd
from skimage.measure import regionprops

# Carregand a imagem
imagem = '104.ge'
imgBGR = cv2.imread(imagem, 1)  # Carregando a imagem colorida
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)  # Convertendo a imagem que esta em BGR para RGB
imgC = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2YCR_CB)  # Convertendo a imagem que esta em BGR para YCrCb
img2 = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2Lab)  # Convertendo a imagem recortada de BGR para Lab

# Realizando a segmentação pelo preocesso de limiarização
R, G, B = cv2.split(imgRGB)  # Segmentando o sistema RGB nos 3 canas R, G e B
Y, Cr, Cb = cv2.split(imgC)
l, a, b = cv2.split(img2)

# Aplicando um filtro no canal R
R = cv2.bilateralFilter(R, 15, 15, 13)

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
    cv2.imwrite(f's{i + 1}({imagem}).png', obj_bgr)
    cv2.imwrite(f'sb{i + 1}({imagem}).png', grao)

    regiao = regionprops(grao)
    area = cv2.contourArea(c)
    perimetro = cv2.arcLength(c, True)
    min_val_r, max_val_r, min_loc_r, max_loc_r = cv2.minMaxLoc(obj_rgb[:, :, 0], mask=grao)
    # min_val_r é o minimo valor de R e min_loc_r e a posição do R
    # max_val_r é o maximo valor de R e o max_loc_r e a posição do R
    med_val_r = cv2.mean(obj_rgb[:, :, 0], mask=grao)
    # med_val_r e a média do R
    min_val_g, max_val_g, min_loc_g, max_loc_g = cv2.minMaxLoc(obj_rgb[:, :, 1], mask=grao)
    med_val_g = cv2.mean(obj_rgb[:, :, 1], mask=grao)
    min_val_b, max_val_b, min_loc_b, max_loc_b = cv2.minMaxLoc(obj_rgb[:, :, 2], mask=grao)
    med_val_b = cv2.mean(obj_rgb[:, :, 2], mask=grao)

    # Criando e salvando os dados em uma tabela
    razao = regiao[0].major_axis_length / regiao[0].minor_axis_length
    dimen += [[str(i + 1), str(h), str(w), str(area), str(razao), str(len(cnts)), str(regiao[0].minor_axis_length),
               str(regiao[0].major_axis_length)]]
    dados = pd.DataFrame(dimen)
    dados = dados.rename(columns={0: 'Grãos', 1: 'Altura', 2: 'Largura', 3: 'Area', 4: 'Razão', 5: 'N de grãos',
                                  6: 'Eixo menor', 7: 'Eixo maior'})
    dados.to_csv(f'Medidas({imagem}).csv', index=False)
