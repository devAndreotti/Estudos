import cv2
import numpy as np
import time

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

matriz1 = cv2.getRotationMatrix2D( (dim_img[0]/2 ,dim_img[1]/2), 90, 1)

# A função cv2.warpAffine() aplica a transformação à imagem original. Recebe como parâmetros:
# - A imagem original
# - A matriz de transformação
# - O tamanho da imagem de saída
ImagemRotacionadaCentro = cv2.warpAffine( imagemOriginal, matriz1, (dim_img[0], dim_img[1]) )

cv2.imshow("Imagem Rotacionada pelo Centro", ImagemRotacionadaCentro)

# Adicionando animação de rotação
# Carregar a imagem
imagem = cv2.imread("folha_colorida.jpg")
if imagem is None:
    raise FileNotFoundError("A imagem não foi encontrada. Verifique o caminho do arquivo.")

dim_img = imagem.shape[:2]  # Dimensões da imagem (altura, largura)


incremento = 3
angulo = incremento
# Loop para criar a animação
while True:
    # Calcular a matriz de rotação para o ângulo atual
    matriz_rotacao = cv2.getRotationMatrix2D((dim_img[1] / 2, dim_img[0] / 2), angulo, 1.4)

    # Aplicar a rotação na imagem
    imagem_rotacionada = cv2.warpAffine(imagem, matriz_rotacao, (dim_img[1], dim_img[0]))

    # Exibir a imagem rotacionada
    cv2.imshow("Girando uma imagem", imagem_rotacionada)

    # Aguardar 0.05 segundos
    if cv2.waitKey(5) & 0xFF == 27:  # Pressionar ESC para sair
        break
    angulo += incremento
    if angulo > 360:
        angulo = incremento

cv2.destroyAllWindows()