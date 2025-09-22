import	cv2

# imgOriginalModelo	=	cv2.imread("folha_colorida.jpg")
imgOriginalModelo	=	cv2.imread("modelo_ruido.jpg")

# Parâmetros:
# src - imagem fonte (input).
# dst - imagem destino (output).
# d - Diâmetro do pixel vizinho que será usado durante o filtro.
# sigmaColor - Filtro sigma no espaço de cor. Quanto maior o valor, mais cores serão misturadas.
# sigmaSpace - Filtro sigma no espaço coordenado. Quanto maior o valor, mais pixels distantes serão misturados.
# imgTratadaModelo     =	cv2.bilateralFilter(imgOriginalModelo, 9, 100, 100)
imgTratadaModelo	=	cv2.bilateralFilter(imgOriginalModelo, 17, 75, 75)

cv2.imshow("Original",	imgOriginalModelo)
cv2.imshow("Filtro Bilateral", imgTratadaModelo)

# cv2.imshow("Original Modelo",	imgOriginalModelo)
# cv2.imshow("Filtro Bilateral Modelo", imgTratadaModelo)

cv2.imwrite("modelo_ruido_tratada.jpg", imgTratadaModelo)
cv2.waitKey(0)
cv2.destroyAllWindows()