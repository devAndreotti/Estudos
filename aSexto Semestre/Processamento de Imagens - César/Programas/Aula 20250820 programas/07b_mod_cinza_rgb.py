'''
Faça um programa em Python, utilizando OpenCV, que modifique o canal de tons de cinza de uma imagem colorida.
Haverá uma barra deslizante para ajustar o nível de modificação.
'''

import cv2
import	numpy	as	np


cv2.namedWindow("Imagem em Tons de Cinza Modificada")
cv2.createTrackbar("CTE_CINZA", "Imagem em Tons de Cinza Modificada", 0, 255, lambda x: None)

# Lendo a imagem
imagem = cv2.imread("frutas.png")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

while True:
    CTE_CINZA = cv2.getTrackbarPos("CTE_CINZA", "Imagem em Tons de Cinza Modificada")

    imagem_cinza_modificada = cv2.subtract(imagem_cinza, CTE_CINZA)
    cv2.imshow("Imagem em Tons de Cinza Modificada", imagem_cinza_modificada)
    if cv2.waitKey(1) & 0xFF == 27:  # Pressione 'Esc' para sair
        break

    cv2.imshow("Imagem Original", imagem)
    cv2.imshow("Imagem em Tons de Cinza", imagem_cinza)
    cv2.imshow("Imagem em Tons de Cinza Modificada", imagem_cinza_modificada)

