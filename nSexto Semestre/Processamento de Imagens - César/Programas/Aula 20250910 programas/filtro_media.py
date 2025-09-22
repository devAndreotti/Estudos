import	cv2

# cv2.blur(src, dst, ksize, anchor, borderType)

# Parameters:

# src - imagem fonte (input).
# dst - imagem destino (output).
# ksize - tamanho do núcleo.
# anchor - ponto de referência.
# borderType - tipo de borda para a imagem de saida/destino.

# imgOriginal	=	cv2.imread("moedas.jpg")
imgOriginal	=	cv2.imread("modelo_ruido.jpg")
# imgTratada	=	cv2.blur(imgOriginal,	(3,3))
imgTratada	=	cv2.blur(imgOriginal,	(7,7))
cv2.imshow("Original",	imgOriginal)
cv2.imshow("Filtro Media",	imgTratada)
cv2.waitKey(0)
cv2.destroyAllWindows()