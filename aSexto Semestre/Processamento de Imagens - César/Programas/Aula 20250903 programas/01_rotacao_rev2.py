import cv2
import numpy as np
import time

# Função de callback para os trackbars (não faz nada, mas é necessária)
def nothing(x):
    pass

# Carregar a imagem
imagem = cv2.imread("folha_colorida.jpg")
if imagem is None:
    raise FileNotFoundError("A imagem não foi encontrada. Verifique o caminho do arquivo.")

dim_img = imagem.shape[:2]  # Dimensões da imagem (altura, largura)

# Criar uma janela para os sliders
cv2.namedWindow("Controles")

# Adicionar sliders para controlar o incremento e o atraso
cv2.createTrackbar("Incremento", "Controles", 1, 10, nothing)  # Incremento de 0 a 10 graus
cv2.createTrackbar("Atraso (ms)", "Controles", 10, 200, nothing)  # Atraso de 10 a 200 ms

angulo = 0

# Loop para criar a animação
while True:
    # Obter os valores dos sliders
    incremento = max(1, cv2.getTrackbarPos("Incremento", "Controles"))
    atraso = max(10, cv2.getTrackbarPos("Atraso (ms)", "Controles"))

    # Garantir que os valores dos sliders não sejam menores que os mínimos
    if cv2.getTrackbarPos("Incremento", "Controles") < 1:
        cv2.setTrackbarPos("Incremento", "Controles", 1)
    if cv2.getTrackbarPos("Atraso (ms)", "Controles") < 10:
        cv2.setTrackbarPos("Atraso (ms)", "Controles", 10)

    # Calcular a matriz de rotação para o ângulo atual
    matriz_rotacao = cv2.getRotationMatrix2D((dim_img[1] / 2, dim_img[0] / 2), angulo, 1.4)

    # Aplicar a rotação na imagem
    imagem_rotacionada = cv2.warpAffine(imagem, matriz_rotacao, (dim_img[1], dim_img[0]))

    # Exibir a imagem rotacionada
    cv2.imshow("Girando uma Imagem", imagem_rotacionada)

    # Aguardar pelo atraso especificado
    if cv2.waitKey(atraso) & 0xFF == 27:  # Pressionar ESC para sair
        break

    # Atualizar o ângulo
    angulo += incremento
    if angulo >= 360:
        angulo -= 360

cv2.destroyAllWindows()