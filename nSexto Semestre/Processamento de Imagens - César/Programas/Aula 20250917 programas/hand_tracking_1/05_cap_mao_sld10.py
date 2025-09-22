import cv2
import mediapipe as mp 
# from cv2 import cv2
import time

aTempo = 0 # tempo anterior
pTempo = 0 # tempo presente

cap = cv2.VideoCapture(0)

#
# Importa API
#
mpMaos = mp.solutions.hands

#
# Criando objeto mao
#

maos = mpMaos.Hands()
#
# Método para desenhar as referencias
#

mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    # Invertendo a imagem
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resultado = maos.process(imgRGB)

    if resultado.multi_hand_landmarks:
        for maosLista in resultado.multi_hand_landmarks:
            for id, mr in enumerate(maosLista.landmark):
                h, w, c = img.shape
                cx, cy = int(mr.x*w), int(mr.y*h)
                print(id, cx, cy)
                if id == 4:
                    cv2.circle(img, (cx, cy), 20, (255, 5, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, maosLista, mpMaos.HAND_CONNECTIONS)
          
    pTempo = time.time()
    fps = 1/(pTempo - aTempo)
    aTempo = pTempo
    cv2.putText(img, str(int(fps)), (10,40), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 3 )
    
    cv2.imshow("Camera", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if cv2.getWindowProperty('Camera',cv2.WND_PROP_VISIBLE) <= 0:
        break
cv2.destroyAllWindows()