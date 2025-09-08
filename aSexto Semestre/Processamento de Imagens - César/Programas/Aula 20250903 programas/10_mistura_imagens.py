import cv2

imagemFichasVermelhas	=	cv2.imread("fichas_vermelhas.jpg")
imagemFichasPretas	    =	cv2.imread("fichas_pretas.jpg")

# Parâmetros da função cv2.addWeighted
# - src1: primeira imagem de entrada
# - alpha: peso da primeira imagem
# - src2: segunda imagem de entrada
# - beta: peso da segunda imagem
# - gamma: valor escalar adicionado ao resultado
imagem	=	cv2.addWeighted(imagemFichasPretas,	1.0,	imagemFichasVermelhas,	0.5,	0)

cv2.imshow("Resultado",	imagem)
cv2.imshow("Fichas Vermelhas",	imagemFichasVermelhas)
cv2.imshow("Fichas Pretas",	imagemFichasPretas)

cv2.waitKey(0)
cv2.destroyAllWindows()