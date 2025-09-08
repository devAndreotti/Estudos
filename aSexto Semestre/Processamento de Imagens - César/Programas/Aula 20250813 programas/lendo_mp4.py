import	cv2

captura	=	cv2.VideoCapture("mov_0035.mp4")

while True:
	Ret, frame = captura.read( )
	cv2.imshow("Video", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

captura.release()
cv2.destroyAllWindows()