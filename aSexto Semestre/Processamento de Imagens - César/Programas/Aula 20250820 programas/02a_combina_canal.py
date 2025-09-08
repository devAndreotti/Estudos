import cv2

# Carregando imagem RGB e segmentando canais

imagem= cv2.imread("frutas.png")

azul, verde, vermelho = cv2.split(imagem)

# Combinando os três canais em uma única imagem

imagem_combinada = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem Combinada", imagem_combinada)

cv2.waitKey(0)
cv2.destroyAllWindows()