import cv2

imagem = cv2.imread("frutas.png")
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

matiz, saturacao, intensidade = cv2.split(imagem_hsv)

cv2.imshow("Canal H", matiz)
cv2.imshow("Canal S", saturacao)
cv2.imshow("Canal V", intensidade)

imagem_recomb = cv2.merge((matiz, saturacao, intensidade))
imagem_rgb = cv2.cvtColor(imagem_recomb, cv2.COLOR_HSV2BGR)

cv2.imshow("Imagem Recombinada", imagem_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()