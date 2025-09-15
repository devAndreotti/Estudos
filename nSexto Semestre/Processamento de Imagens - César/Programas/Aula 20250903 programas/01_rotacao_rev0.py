import cv2
import numpy as np

#
# Rotaciona Imagem tons Cinza
#

# imagemOriginal	=	cv2.imread("folha_colorida.jpg",0)
# (totalLinhas,	totalColunas)	=	imagemOriginal.shape
# matriz	=	cv2.getRotationMatrix2D((totalColunas	/	2 ,	totalLinhas	/	2 ), 90, 1)
# ImagemRotacionada=cv2.warpAffine(	imagemOriginal,  matriz, (totalColunas,	totalLinhas) )

# cv2.imshow("Resultado",	ImagemRotacionada)
# cv2.imshow("Imagem Original",imagemOriginal)

#
# Rotaciona Imagem Colorida
#


imagemOriginal = cv2.imread("folha_colorida.jpg")
cv2.imshow("Imagem Original", imagemOriginal)

dim_img = imagemOriginal.shape

print(dim_img)

# OU: (Altura, Largura) = image.shape[:2]

# dim_img:  (Height, Width, # Channels)
# A função cv2.getRotationMatrix2D() recebe os seguintes parâmetros:
# - O centro de rotação (x, y)
# - O ângulo de rotação (em graus)
# - O fator de escala

matriz1 = cv2.getRotationMatrix2D( (dim_img[0]/2 ,dim_img[1]/2), 90, 1.0)

# A função cv2.warpAffine() aplica a transformação à imagem original. Recebe como parâmetros:
# - A imagem original
# - A matriz de transformação
# - O tamanho da imagem de saída
ImagemRotacionadaCentro = cv2.warpAffine( imagemOriginal, matriz1, (dim_img[0], dim_img[1]) )

cv2.imshow("Imagem Rotacionada pelo Centro", ImagemRotacionadaCentro)

cv2.waitKey(0)
cv2.destroyAllWindows()