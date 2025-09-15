import cv2

# Lendo os canais
matiz = cv2.imread("frutas_canal_h.jpg", cv2.IMREAD_GRAYSCALE)
saturacao = cv2.imread("frutas_canal_s.jpg", cv2.IMREAD_GRAYSCALE)
intensidade = cv2.imread("frutas_canal_v.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Canal H", matiz)
cv2.imshow("Canal S", saturacao)
cv2.imshow("Canal V", intensidade)

imagem_recomb = cv2.merge((matiz, saturacao, intensidade))
imagem_rgb = cv2.cvtColor(imagem_recomb, cv2.COLOR_HSV2BGR)

cv2.imshow("Imagem Recombinada", imagem_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()