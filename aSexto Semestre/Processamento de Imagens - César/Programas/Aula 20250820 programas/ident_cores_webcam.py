import cv2
import	numpy	as	np


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # cv2.flip(frame, 0) → espelha verticalmente (eixo x).

    # cv2.flip(frame, 1) → espelha horizontalmente (eixo y).

    # cv2.flip(frame, -1) → espelha tanto horizontal quanto vertical.

    frame = cv2.flip(frame, 1)
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #vermelho

    # tomClaro	=	np.array([120,	100,	100])
    # tomEscuro	=	np.array([200,	255,	255])

    # azul

    tomClaro	=	np.array([100, 100, 120])
    tomEscuro	=	np.array([255, 255,	200])

    # # verde

    # tomClaro	=	np.array([40,	100,	100])
    # tomEscuro	=	np.array([80,	255,	255])


    imgSegmentada	=	cv2.inRange(hsv_frame,	tomClaro,	tomEscuro)
    cv2.imshow("Segmentada",	imgSegmentada)

    cv2.imshow("Quadro", frame)
    key = cv2.waitKey(1) 
    if key == 27: # Tecla ESC
        break

cap.release()
cv2.destroyAllWindows()