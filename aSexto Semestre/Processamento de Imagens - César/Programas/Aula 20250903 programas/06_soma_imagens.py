import	cv2

imagemFichasVermelhas = cv2.imread("fichas_vermelhas.jpg")
imagemFichasPretas = cv2.imread("fichas_pretas.jpg")
imagem = cv2.add(imagemFichasPretas, imagemFichasVermelhas)

cv2.imshow("Fichas Vermelhas", imagemFichasVermelhas)
cv2.imshow("Fichas Pretas", imagemFichasPretas)
cv2.imshow("Resultado Soma Imagens", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()