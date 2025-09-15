import cv2

# Combinando os três canais em uma única imagem
# Lendo os arquivos que tem os canais de cores RGB
# frutas-canal-azul.jpeg
# frutas-canal-verde.jpeg
# frutas-canal-vermelho.jpeg

azul = cv2.imread("frutas-canal-azul.jpeg", cv2.IMREAD_GRAYSCALE)
verde = cv2.imread("frutas-canal-verde.jpeg", cv2.IMREAD_GRAYSCALE)
vermelho = cv2.imread("frutas-canal-vermelho.jpeg", cv2.IMREAD_GRAYSCALE)

imagem_combinada = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem Combinada", imagem_combinada)

cv2.waitKey(0)
cv2.destroyAllWindows()