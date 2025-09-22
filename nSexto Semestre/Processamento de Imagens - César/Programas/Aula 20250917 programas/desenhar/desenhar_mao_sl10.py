import cv2
import numpy as np
import time
import os
import mrm

#
# Diretorio com as Imagens
#

camImg = "img"

#
# Parametros Posicao da Paleta de Cor
#
espX = 250
dx = 100
espY = 10

#
# Parametros Linha e Ponto Inicial
#

expessuraLinha = 5
xInicial, yInicial = 0, 0

nomeCoresImage = os.listdir(camImg)
#print(nomeCoresImage)
listaCores = []
for imgDir in nomeCoresImage:
    corImagem = cv2.imread(f'{camImg}/{imgDir}')
    listaCores.append(corImagem)
#print(len(listaCores))
alt, larg, cor = listaCores[0].shape
#print(alt, larg, cor)


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4,720)

#
# Numero de quadros por segundo (QPS)
# qps = 1 / (tempo_agora - tempo_anterior)
#

tAnt = 0

#
# Carregamento Classe Deteccao Mao - Media Pipe
#
detetor = mrm.deteccaoMao(certezadeteccao=0.85)

#
# Cor Default inicial - Vermelha
# 
corPintar = (0, 0, 255)

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
        # Posiçoes dedos indicador e medio
        #
        xI, yI = listaInfoMao[8][1:]
        xM, yM = listaInfoMao[12][1:]
        #print(xI, yI, xM, yM)
        
        posDedosMao = detetor.identificaDedosLevantados(listaInfoMao)
        #print(posDedosMao)

        if posDedosMao[1] and posDedosMao[2]:
            cv2.rectangle(img, (xI, yI-25), (xM, yM+25), corPintar, cv2.FILLED)
            #print("Modo Selecao")
            #
            # Selecionando as regioes da cor
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
            cv2.line(img, (xInicial, yInicial), (xI, yI), corPintar, expessuraLinha)
            xInicial, yInicial = xI, yI
            print("Modo Desenho")


    #
    # Carregando Cores
    #
    for i in range(4):
        img[espY: espY+alt, espX + i*(larg+dx): espX + i*dx+ (i+1)*larg] = listaCores[i]
     
    
    tAtual = time.time()
    qps = 1 / (tAtual - tAnt)
    tAnt = tAtual
    
        
    cv2.putText(img, f'QPS:{int(qps)}', (20, 55), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 10, 40), 3)

    cv2.imshow("Camera", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if cv2.getWindowProperty('Camera',cv2.WND_PROP_VISIBLE) <= 0:
        break
cv2.destroyAllWindows()
