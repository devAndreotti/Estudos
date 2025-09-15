import	cv2
import	numpy as np

imagemOriginal	=	cv2.imread("folha_colorida.jpg")
# Os parâmetros de cv2.resize são:
# - imagem: a imagem de entrada
# - dsize: a nova dimensão da imagem (largura, altura): se for None, usa os fatores de escala
# - fx: fator de escala na direção x: se for 0, usa o valor de dsize
# - fy: fator de escala na direção y: se for 0, usa o valor de dsize
# - interpolation: método de interpolação
imagemModificada	=	cv2.resize( imagemOriginal,	None,
                                    fx	=	2.5,	fy	=	0.5,
                                    interpolation	=	cv2.INTER_CUBIC)

cv2.imshow("Original",	imagemOriginal)
cv2.imshow("Resultado",	imagemModificada)

cv2.waitKey(0)
cv2.destroyAllWindows()