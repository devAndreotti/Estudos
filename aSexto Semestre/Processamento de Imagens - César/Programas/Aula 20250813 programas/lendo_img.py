import cv2

img_lida = cv2.imread("house.jpg")
cv2.imshow("Formas de Captura", img_lida)
cv2.waitKey(0)
cv2.destroyAllWindows()
