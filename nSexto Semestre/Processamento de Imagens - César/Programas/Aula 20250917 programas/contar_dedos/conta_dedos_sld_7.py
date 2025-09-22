'''
Melhorias deste programa em relação ao anterior:
i) Identifica o número de dedos levantados na mão esquerda imprimindo na tela
'''

# Importação das bibliotecas
import cv2 as cv2

# Importação da biblioteca time para medir o tempo entre os quadros
import time

# Importação da biblioteca os para manipulação de arquivos
import os

# Importação da biblioteca mrm que contém a classe deteccaoMao
import mrm

# Largura e altura da imagem da webcam
lCam, aCam = 640, 480

# Fator de escala a ser aplicado nas imagens de dedos
f_escala = 0.4

# Inicialização da webcam
cap = cv2.VideoCapture(0)
cap.set(3, lCam)
cap.set(4, aCam)

# Diretório das imagens de dedos
camDiretorio = "img"

# Armazena em uma lista todos os itens na pasta
arqImgDedos = os.listdir(camDiretorio)
print(arqImgDedos)

#
#Carregando as imagens dos dedos da maos
#

# Variável para armazenar as imagens de dedos
imgDedos = []
for nomeImg in arqImgDedos:
    imagem = cv2.imread(f'{camDiretorio}/{nomeImg}')
    print(f'{camDiretorio}/{nomeImg}')
    alt, larg, cor = imagem.shape
    n_larg, n_alt = int(f_escala*larg), int(f_escala*alt)
    dim = (n_larg, n_alt)
    nova_imagem = cv2.resize(imagem, dim, interpolation = cv2.INTER_AREA)
    imgDedos.append(nova_imagem)

#
# Numero de quadros por segundo (QPS)
# qps = 1 / (tempo_agora - tempo_anterior)
#
tAnt = 0

#
# Carregamento Classe Deteccao Mao - Media Pipe
#
detetor = mrm.deteccaoMao()

#
# Pontos de Referencia das pontas dos dedos
#
prDedosmao = [8, 12, 16, 20]

while True:
    success, img = cap.read()

    # Invertendo a imagem
    img = cv2.flip(img, 1)
    img = detetor.encontreMaos(img)
    listaInfoMao = detetor.encontreReferencias(img, desenhar = False)
    #print(listaInfoMao)
    
    # Verificando se mao foi detectada

    if len(listaInfoMao) != 0:
        numDedosLevantados = 0
        for id in range(0, 4):
            if listaInfoMao[prDedosmao[id]][2] < listaInfoMao[prDedosmao[id]-2][2]:
                numDedosLevantados += 1
        #
        # Testando o dedao
        #

        if listaInfoMao[4][1] > listaInfoMao[2][1]:
            numDedosLevantados += 1


        print (numDedosLevantados)


    # variável que indicará o número do dedo a ser exibido
    # se igual a 0 a imagem será a da mão fechada
    num_dedo = 4
    img[0:n_alt, 0:n_larg] = imgDedos[num_dedo]


    # Calcula o número de quadros por segundo (QPS)
    tAtual = time.time()
    qps = 1 / (tAtual - tAnt)
    tAnt = tAtual
    
    # Exibe o QPS na tela
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