'''
Melhorias deste programa em relação ao anterior:
i) Exibe o número de quadros por segundo (QPS) na imagem da webcam
'''

# Importação das bibliotecas
import cv2 as cv2

# Importação da biblioteca time para medir o tempo entre os quadros
import time
import os

# Importação da biblioteca mrm que contém a classe deteccaoMao
import mrm

# Largura e altura da imagem da webcam
lCam, aCam = 1280, 960

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

#
# Numero de quadros por segundo (QPS)
# qps = 1 / (tempo_agora - tempo_anterior)
#

# Varriável para armazenar o tempo atual
tAnt = 0

# Carrega a classe deteccaoMao
detetor = mrm.deteccaoMao()


while True:
    success, img = cap.read()
    # inverte a imagem
    img = cv2.flip(img, 1)
    img = detetor.encontreMaos(img)

    # listaInfoMao contém as informações da(s) mão(õs) detectada(s)
    listaInfoMao = detetor.encontreReferencias(img, desenhar = False)
    print(listaInfoMao)
    
    # variável que indicará o número do dedo a ser exibido
    # se igual a 0 a imagem será a da mão fechada
    num_dedo = 2
    img[0:n_alt, 0:n_larg] = imgDedos[num_dedo]

    # Calcula o número de quadros por segundo (QPS)
    tAtual = time.time()
    qps = 1 / (tAtual - tAnt)
    tAnt = tAtual

    # Exibe o número de quadros por segundo (QPS) na imagem da webcam  
    cv2.putText(img, f'QPS:{int(qps)}', (520, 25), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 10, 40), 3)
    
    cv2.imshow("Imagem Web Cam", img)
    cv2.waitKey(1)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if cv2.getWindowProperty('Imagem Web Cam',cv2.WND_PROP_VISIBLE) <= 0:
        break
cv2.destroyAllWindows()