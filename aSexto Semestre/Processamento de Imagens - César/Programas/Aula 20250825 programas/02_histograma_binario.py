import	cv2
import  numpy as np
import matplotlib.pyplot as grafico
#
# Outra forma de utilizar:
#
# from matplotlib import pyplot as grafico
#

#
# 1) Conta o número de pixel nas cores 0 (preto) e 255 (branco)
#

imagem = cv2.imread("folha_binaria.bmp",cv2.IMREAD_GRAYSCALE)
print("altura:", imagem.shape[0], "largura:", imagem.shape[1])
totalPixelsPreto = 0;
totalPixelsBranco = 0;
for	y in range(0, imagem.shape[0]):
    for	x in range(0, imagem.shape[1]):
        if	imagem[y,x] == 255:
            totalPixelsBranco += 1;
        # else:
        #     totalPixelsPreto += 1;
print(totalPixelsBranco)
# print(totalPixelsPreto)
print(imagem.shape[0]*imagem.shape[1]-totalPixelsBranco)


#
# 2) Utilizando a função hist da biblioteca Matplotlib
# Param #1 - Método ravel(): como a imagem é um arranjo 2D, o 
# método ravel() o converte para um arranjo 1D.break
# Param #2 - número de faixas
# Param #3 - faixa a ser considerada

grafico.hist(imagem.ravel(), 16, [0,256])

cv2.imshow("Folha Binaria", imagem)
grafico.show()

