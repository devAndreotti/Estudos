import cv2
import numpy as np

imagemOriginal = cv2.imread("folha_colorida.jpg")
cv2.imshow("Imagem Original", imagemOriginal)

dim_img = imagemOriginal.shape[:2]

center_h = 100
center_w = 200

# Criar matrizes de translação
# Recebe como parâmetros:
# - center_w: coordenada x do centro de rotação
# - center_h: coordenada y do centro de rotação

matriz_t1 = np.float32([[1,	0, -center_w],	[0, 1, -center_h]])
matriz_t2 = np.float32([[1,	0, center_w],	[0, 1, center_h]])

imagemDeslocada1	= cv2.warpAffine(imagemOriginal, matriz_t1, dim_img)
# matrizR         = cv2.getRotationMatrix2D( (dim_img[0]/2 ,dim_img[1]/2), 45, 1)
ImagemRotacionada = cv2.warpAffine( imagemDeslocada1, matrizR, dim_img)
# imagemDeslocada2	= cv2.warpAffine(ImagemRotacionada, matriz_t2, dim_img)

cv2.imshow("Imagem Rotacionada", ImagemRotacionada)

cv2.waitKey(0)
cv2.destroyAllWindows()