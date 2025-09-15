import	cv2
import  numpy as np
import matplotlib.pyplot as grafico
#
# Outra forma de utilizar:
#
# from matplotlib import pyplot as grafico
#

imagem = cv2.imread("folha_tons_cinza.jpg",cv2.IMREAD_GRAYSCALE)

#
# 1) Utilizando a função hist da biblioteca Matplotlib:
# Param #1 - Método ravel(): como a imagem é um arranjo 2D, o 
# método ravel() o converte para um arranjo 1D.break
# Param #2 - número de faixas.
# Param #3 - faixa a ser considerada.

grafico.hist(imagem.ravel(), 256, [0,256])
grafico.title("Histrograma Tons Cinza")
grafico.xlabel("Intensidade")
grafico.ylabel("QTD")
grafico.text(50, 25000, "folha_tons_cinza.jpg")
grafico.xlim(0,255)
grafico.grid(True)

cv2.imshow("Folha Tons Cinza", imagem)
grafico.show()

