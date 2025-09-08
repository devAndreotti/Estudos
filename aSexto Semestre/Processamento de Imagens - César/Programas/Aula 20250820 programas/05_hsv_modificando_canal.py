import cv2

CTE = 10

# Carregando imagem RGB
imagem = cv2.imread("frutas.png")

# Convertendo RGB para HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Segmentando canais H, S e V
matiz, saturacao, intensidade = cv2.split(imagem_hsv)

saturacao_plus = saturacao + CTE
saturacao_minus = saturacao - CTE

imagem_plus =cv2.merge((matiz, saturacao_plus, intensidade))
imagem_minus=cv2.merge((matiz, saturacao_minus, intensidade))

imagem_plus_rgb = cv2.cvtColor(imagem_plus, cv2.COLOR_HSV2BGR)
imagem_minus_rgb = cv2.cvtColor(imagem_minus, cv2.COLOR_HSV2BGR)

# Exibindo imagem alterada
cv2.imshow("Imagem Plus", imagem_plus_rgb)
cv2.imshow("Imagem Minus", imagem_minus_rgb)
cv2.imshow("Imagem Original", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()