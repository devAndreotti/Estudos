import cv2

imagemFichasVermelhas	=	cv2.imread("fichas_vermelhas.jpg")
imagemFichasPretas	    =	cv2.imread("fichas_pretas.jpg")

# Parâmetros da função cv2.multiply
# - imagemFichasPretas: primeira imagem de entrada
# - cte (Opcional: se especificado, será multiplicado por cada pixel da imagem)
# - imagemFichasVermelhas: segunda imagem de entrada
# - dst: imagem de saída
# - scale: fator de escala, aplicado a cada pixel da imagem dst
imagem	=	cv2.multiply(imagemFichasPretas,	0.5,	dst=imagemFichasVermelhas,	scale=0.5)

cv2.imshow("Resultado",	imagem)
cv2.imshow("Fichas Vermelhas",	imagemFichasVermelhas)
cv2.imshow("Fichas Pretas",	imagemFichasPretas)

cv2.waitKey(0)
cv2.destroyAllWindows()