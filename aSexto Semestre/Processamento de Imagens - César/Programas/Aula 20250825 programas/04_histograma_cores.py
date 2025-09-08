import	cv2
import  numpy as np
import matplotlib.pyplot as grafico
#
# Outra forma de utilizar:
#
# from matplotlib import pyplot as grafico
#

imagem = cv2.imread("folha_colorida.jpg")
azul, verde, vermelho = cv2.split(imagem)

grafico.title("Histrograma AZUL")
grafico.xlabel("Intensidade")
grafico.ylabel("QTD")
grafico.text(50, 25000, "folha_colorida.jpg")
grafico.xlim(0,255)
grafico.grid(True)
grafico.hist(azul.ravel(), 256, [0,255])

grafico.figure()
grafico.title("Histrograma VERDE")
grafico.xlabel("Intensidade")
grafico.ylabel("QTD")
grafico.text(50, 25000, "folha_colorida.jpg")
grafico.xlim(0,255)
grafico.grid(True)
grafico.hist(verde.ravel(), 256, [0,255])

grafico.figure()
grafico.title("Histrograma VERMELHO")
grafico.xlabel("Intensidade")
grafico.ylabel("QTD")
grafico.text(50, 25000, "folha_colorida.jpg")
grafico.xlim(0,255)
grafico.grid(True)
grafico.hist(vermelho.ravel(), 256, [0,255])

cv2.imshow("Folha Colorida", imagem)
grafico.show()