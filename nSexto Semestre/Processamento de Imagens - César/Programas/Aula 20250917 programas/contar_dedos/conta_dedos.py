'''
Este código:
i) captura a imagem da webcam
ii) redimensiona a imagem da webcam
iii) carrega imagens de dedos de 1 a 5 armazenadas no diretório "img"
iv) redimensiona as imagens de dedos
v) exibe a imagem da webcam com a imagem de um dedo no canto superior esquerdo
'''

# Importação das bibliotecas
import cv2 as cv2
import time
import os

lCam, aCam = 640, 480

# Fator de escala a ser aplicado nas imagens de dedos
f_escala = 0.4

# Inicialização da webcam
cap = cv2.VideoCapture(0)
cap.set(3, lCam)
cap.set(4, aCam)

# Diretório das imagens de dedos
camDiretorio = "img"

arqImgDedos = os.listdir(camDiretorio)
print(arqImgDedos)

# Variável para armazenar as imagens de dedos
imgDedos = []

# Carrega as imagens de dedos e as redimensiona
for nomeImg in arqImgDedos:
    imagem = cv2.imread(f'{camDiretorio}/{nomeImg}')
    print(f'{camDiretorio}/{nomeImg}')
    alt, larg, cor = imagem.shape
    n_larg, n_alt = int(f_escala*larg), int(f_escala*alt)
    dim = (n_larg, n_alt)
    nova_imagem = cv2.resize(imagem, dim, interpolation = cv2.INTER_AREA)
    imgDedos.append(nova_imagem)

# Exibe a imagem da webcam com a imagem de um dedo no canto superior esquerdo
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # variável que indicará o número do dedo a ser exibido
    # se igual a 0 a imagem será a da mão fechada
    num_dedo = 2
    img[0:n_alt, 0:n_larg] = imgDedos[num_dedo]

    cv2.imshow("Imagem Web Cam", img)
    cv2.waitKey(1)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if cv2.getWindowProperty('Imagem Web Cam',cv2.WND_PROP_VISIBLE) <= 0:
        break
cv2.destroyAllWindows()