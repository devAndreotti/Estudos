import cv2

# Carregando imagem RGB
imagem = cv2.imread("frutas.png")

# Convertendo RGB para HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Segmentando canais H, S e V
matiz, saturacao, intensidade = cv2.split(imagem_hsv)

# Exibindo imagens dos canais separados
cv2.imshow("Canal H", matiz)
cv2.imshow("Canal S", saturacao)
cv2.imshow("Canal V", intensidade)

# Exibindo imagem original
cv2.imshow("Imagem Original", imagem)

# Salvando os canais separados
cv2.imwrite("frutas_canal_h.jpg", matiz)
cv2.imwrite("frutas_canal_s.jpg", saturacao)
cv2.imwrite("frutas_canal_v.jpg", intensidade)

cv2.waitKey(0)
cv2.destroyAllWindows()