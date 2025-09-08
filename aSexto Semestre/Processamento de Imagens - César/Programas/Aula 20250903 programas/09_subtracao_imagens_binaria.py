import	cv2
import  numpy as np

imagemFichaPosicao1	=	cv2.imread("ficha_posicao_1.jpg")
imagemFichaPosicao2	=	cv2.imread("ficha_posicao_2.jpg")

imagem	=	cv2.subtract(imagemFichaPosicao1, imagemFichaPosicao2)

linhas, col, chan  = imagem.shape
print(linhas, col, chan)

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# Parâmetros da função cv2.threshold
# - src: imagem de entrada (em escala de cinza)
# - thresh: valor de limiar
# - maxval: valor máximo a ser atribuído aos pixels que superam o limiar
# - type: tipo de limiarização
# Retorna uma tupla (retval, dst), onde retval é o valor do limiar usado (útil para métodos automáticos) e dst é a imagem resultante
valor, imagem_binaria = cv2.threshold(imagem_cinza, 25, 255, cv2.THRESH_BINARY)

print("Valor do Limiar: ", valor)
cv2.imshow("Posicao 1",	imagemFichaPosicao1)
cv2.imshow("Posicao 2",	imagemFichaPosicao2)
cv2.imshow("Resultado",	imagem)
cv2.imshow("Cinza", imagem_cinza)
cv2.imshow("Binaria", imagem_binaria)

cv2.waitKey(0)
cv2.destroyAllWindows()