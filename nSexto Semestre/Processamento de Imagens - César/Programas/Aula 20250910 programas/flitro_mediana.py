import	cv2

imgOriginal	=	cv2.imread("modelo_ruido.jpg")
imgTratada	=	cv2.medianBlur(imgOriginal,	9)
cv2.imshow("Original",	imgOriginal)
cv2.imshow("Filtro Mediana",	imgTratada)
cv2.waitKey(0)
cv2.destroyAllWindows()