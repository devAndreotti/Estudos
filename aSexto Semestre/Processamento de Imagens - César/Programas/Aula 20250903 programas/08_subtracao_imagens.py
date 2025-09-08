import	cv2

imagemFichaPosicao1	=	cv2.imread("ficha_posicao_1.jpg")
imagemFichaPosicao2	=	cv2.imread("ficha_posicao_2.jpg")

imagem	=	cv2.subtract(imagemFichaPosicao2, imagemFichaPosicao1)

cv2.imshow("Posicao 1",	imagemFichaPosicao1)
cv2.imshow("Posicao 2",	imagemFichaPosicao2)
cv2.imshow("Resultado",	imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()