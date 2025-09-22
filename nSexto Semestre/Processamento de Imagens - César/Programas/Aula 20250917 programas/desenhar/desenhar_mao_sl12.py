# Importando Bibliotecas
import cv2
import numpy as np
# import time
import os
import mrm

#
# Diretorio com as Imagens
#
camImg = "img"

#
# Parametros Posicao da Paleta de Cor e Borracha que serao desenhadas
#

#espX: Espaçamento entre as imagens
#dx: Espaçamento entre as paletas de cores
#espY: Espaçamento entre a paleta de cores e a area de desenho
espX = 250
dx = 100
espY = 10

#
# Parametros Linha e Ponto Inicial
#
expessuraLinha = 5
expessuraApagar = 30
xInicial, yInicial = 0, 0

# Armazena na lista nomeCoresImage todos os itens na pasta
nomeCoresImage = os.listdir(camImg)

#print(nomeCoresImage)

# Carregando as imagens das cores na lista listaCores
listaCores = []
for imgDir in nomeCoresImage:
    corImagem = cv2.imread(f'{camImg}/{imgDir}')
    listaCores.append(corImagem)
#print(len(listaCores))
alt, larg, cor = listaCores[0].shape
#print(alt, larg, cor)

#
# Var Tamanho Tela
#
Largura = 1280
Altura = 720

# Inicialização da webcam
cap = cv2.VideoCapture(0)
cap.set(3, Largura)
cap.set(4,Altura)

#
# Numero de quadros por segundo (QPS)
# qps = 1 / (tempo_agora - tempo_anterior)
#
tAnt = 0

#
# Carregamento Classe Deteccao Mao - Media Pipe
#
detetor = mrm.deteccaoMao(certezadeteccao=0.5)

#
# Cor Default inicial - Vermelha
# 
corPintar = (0, 0, 255)

#
# Area de Desenho
#

# imgDesenho armazena o desenho em uma segunda camada da imagem que será exibida na tela por meio de uma máscara
imgDesenho = np.zeros((Altura, Largura, 3), np.uint8)

while True:
    success, img = cap.read()
    #
    # Invertendo a img
    #
    img = cv2.flip(img, 1)

    #
    # Deteccao Mao
    #
    img = detetor.encontreMaos(img)
    listaInfoMao = detetor.encontreReferencias(img, desenhar = False)


    if len (listaInfoMao) != 0:
        # print(listaInfoMao)

        #
        # Coordenadas dos dedos indicador e medio
        #
        xI, yI = listaInfoMao[8][1:]
        xM, yM = listaInfoMao[12][1:]
        #print(xI, yI, xM, yM)
        
        posDedosMao = detetor.identificaDedosLevantados(listaInfoMao)
        #print(posDedosMao)

        if posDedosMao[1] and posDedosMao[2]:
            xInicial, yInicial = 0, 0
            cv2.rectangle(img, (xI, yI-25), (xM, yM+25), corPintar, cv2.FILLED)
            #print("Modo Selecao")

            #
            # Verificando se o dedo indicador está dentro de uma área de seleção
            #

            if yM < espY + alt: 
                if  espX <= xM <= espX + larg:
                    print("Vermelho")
                    corPintar = (0, 0, 255)
                elif espX + larg + dx <= xM <= espX + dx + 2*larg:
                    print("Verde")
                    corPintar = (0, 255, 0)
                elif espX + 2*(larg + dx) <= xM <= espX + 2*dx + 3*larg:
                    print("Azul")
                    corPintar = (255, 0, 0)
                elif espX + 3*(larg + dx) <= xM <= espX + 3*dx + 4*larg:
                    print("Preto")
                    corPintar = (0, 0, 0)
        elif posDedosMao[1] and posDedosMao[2] == False:
            cv2.circle(img, (xI, yI), 15, corPintar, cv2.FILLED)
            if xInicial == 0 and yInicial == 0:
                xInicial, yInicial = xI, yI

            if corPintar == (0, 0, 0):
                cv2.line(img, (xInicial, yInicial), (xI, yI), corPintar, expessuraApagar)
                cv2.line(imgDesenho, (xInicial, yInicial), (xI, yI), corPintar, expessuraApagar)
            else:
                cv2.line(img, (xInicial, yInicial), (xI, yI), corPintar, expessuraLinha)
                cv2.line(imgDesenho, (xInicial, yInicial), (xI, yI), corPintar, expessuraLinha)
            xInicial, yInicial = xI, yI
            print("Modo Desenho")
    
    # Convertendo a imagem para escala de cinza
    imgGray = cv2.cvtColor(imgDesenho, cv2.COLOR_BGR2GRAY)

    # Invertendo a imagem
    __, imgInv = cv2.threshold(imgGray, 20, 255, cv2.THRESH_BINARY_INV)

    # Convertendo a imagem para escala de cinza
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

    # Aplicando a mascara and
    # A mascara and é aplicada para que a imagem original seja preservada
    img = cv2.bitwise_and(img, imgInv)

    # Aplicando a mascara or
    # A mascara or é aplicada para que a imagem desenhada seja exibida sobre a imagem original
    img = cv2.bitwise_or(img, imgDesenho)


    #
    # Carregando Cores
    #
    for i in range(4):
        img[espY: espY+alt, espX + i*(larg+dx): espX + i*dx+ (i+1)*larg] = listaCores[i]
     
    #
    # Caso queira exibir a taxa de quadros por segundo descomente as linhas abaixo e a linha que importa a biblioteca time
    #

    # tAtual = time.time()
    # qps = 1 / (tAtual - tAnt)
    # tAnt = tAtual
    
        
    #cv2.putText(img, f'QPS:{int(qps)}', (20, 55), cv2.FONT_HERSHEY_PLAIN,
     #           2, (255, 10, 40), 3)

    cv2.imshow("Camera", img)
    #cv2.imshow("Desenho", imgDesenho)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if cv2.getWindowProperty('Camera',cv2.WND_PROP_VISIBLE) <= 0:
        break
cv2.destroyAllWindows()
