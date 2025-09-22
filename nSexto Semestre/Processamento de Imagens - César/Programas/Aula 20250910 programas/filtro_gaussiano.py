import	cv2

imgOriginal	=	cv2.imread("modelo_ruido.jpg")
imgTratada1	=	cv2.GaussianBlur(imgOriginal, (5,5), 0)
imgTratada2	=	cv2.GaussianBlur(imgOriginal, (7,7), 0)
cv2.imshow("Original",	imgOriginal)
cv2.imshow("Filtro Gaussiano 5x5",	imgTratada1)
cv2.imshow("Filtro Gaussiano 7x7",	imgTratada2)
cv2.waitKey(0)
cv2.destroyAllWindows()