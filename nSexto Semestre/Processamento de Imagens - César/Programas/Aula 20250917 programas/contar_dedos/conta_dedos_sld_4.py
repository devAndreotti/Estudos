'''
Melhorias deste programa em relação ao anterior:
i) Verifica se o diretório das imagens de dedos existe
ii) Verifica se o arquivo de imagem de dedo existe
iii) Exibe uma mensagem de erro caso o arquivo de imagem de dedo não exista
iv) Exibe uma mensagem de erro caso a imagem não seja carregada
'''
import cv2 as cv2
import os

lCam, aCam = 640, 480

# Fator de escala a ser aplicado nas imagens de dedos
f_escala = 0.4

# Inicialização da webcam
cap = cv2.VideoCapture(0)
cap.set(3, lCam)
cap.set(4, aCam)

# Diretório das imagens de dedos
cam_arqImgDedos = 'img'

# Lista todos os itens na pasta
itens = os.listdir(cam_arqImgDedos)

# Lendo apenas os nomes dos arquivos de imagem que estão no diretório cam_arqImgDedos
arqImgDedos = [arquivo for arquivo in itens if os.path.isfile(os.path.join(cam_arqImgDedos, arquivo))]

print(arqImgDedos)

# Variável para armazenar as imagens de dedos
imgDedos = []

# Carrega as imagens de dedos e as redimensiona
for nomeImg in arqImgDedos:
    caminho_imagem = os.path.join(cam_arqImgDedos, nomeImg)
    print(caminho_imagem)
    if not os.path.isfile(caminho_imagem):
        print(f"Erro: o arquivo '{caminho_imagem}' não existe.")
        continue

    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        print(f"Erro ao carregar a imagem {nomeImg}")
    else:
        alt, larg, cor = imagem.shape
        n_larg, n_alt = int(f_escala * larg), int(f_escala * alt)
        dim = (n_larg, n_alt)
        nova_imagem = cv2.resize(imagem, dim, interpolation=cv2.INTER_AREA)
        imgDedos.append(nova_imagem)


# Exibe a imagem da webcam com a imagem de um dedo no canto superior esquerdo
while True:
    success, img = cap.read()
    # inverte a imagem
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