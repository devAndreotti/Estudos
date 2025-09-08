import cv2
import	numpy	as	np

'''
Faça um programa em Python, utilizando OpenCV, que modifique o canal de tons de cinza de uma imagem colorida.
'''

# Criando constante a ser adicionada ao tom de cinza
CTE_CINZA = -10

imagem = cv2.imread("frutas.png")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Modificando o canal de tons de cinza
imagem_cinza_modificada = cv2.add(imagem_cinza, CTE_CINZA)

cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem em Tons de Cinza", imagem_cinza)
cv2.imshow("Imagem em Tons de Cinza Modificada", imagem_cinza_modificada)

cv2.waitKey(0)
cv2.destroyAllWindows()