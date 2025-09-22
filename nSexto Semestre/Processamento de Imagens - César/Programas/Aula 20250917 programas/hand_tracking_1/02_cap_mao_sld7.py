import cv2
import mediapipe as mp 
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
    # Invertendo a imagem para mostrar a imagem correta
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resultado = maos.process(imgRGB)

    if resultado.multi_hand_landmarks:
        #print(resultado.multi_hand_landmarks)
        for maosLista in resultado.multi_hand_landmarks:
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