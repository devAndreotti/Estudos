import	cv2

captura	=	cv2.VideoCapture(0)

while True:
	Ret, frame = captura.read( )
	cv2.imshow("WebCam", frame)

	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

captura.release()
cv2.destroyAllWindows()