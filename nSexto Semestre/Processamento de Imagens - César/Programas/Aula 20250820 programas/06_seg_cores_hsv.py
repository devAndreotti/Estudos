import cv2
import	numpy	as	np

imagemRGB = cv2.imread("cubo_magico.jpg")
imagemHSV = cv2.cvtColor(imagemRGB, cv2.COLOR_BGR2HSV)

#vermelho
# tomClaro	=	np.array([80,	110,	110])
# tomEscuro	=	np.array([200,	255,	255])

# amarelo
# tomClaro	=	np.array([10, 100, 100])
# tomEscuro	=	np.array([50, 255,	255])

# verde
tomClaro	=	np.array([40,	100,	100])
tomEscuro	=	np.array([80,	255,	255])

imgSegmentada=cv2.inRange(imagemHSV, tomClaro, tomEscuro)
cv2.imshow("Segmentada", imgSegmentada)
cv2.imshow("Original", imagemRGB)

cv2.waitKey(0)
cv2.destroyAllWindows()