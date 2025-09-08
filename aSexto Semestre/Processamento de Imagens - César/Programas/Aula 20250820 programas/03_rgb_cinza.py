import cv2

#	Carregando	imagem	RGB	e	segmentando	canais

imagem = cv2.imread("frutas.jpg")

# Convertendo para tons de cinza

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

cv2.imshow("Imagem Tons de Cinza", imagem_cinza)
cv2.imshow("Imagem Original", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()