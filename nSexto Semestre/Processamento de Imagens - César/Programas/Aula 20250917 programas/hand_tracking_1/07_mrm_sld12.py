import mediapipe as mp 
import time
import mrm_sld11 as mrm
import cv2

aTempo = 0 # tempo anterior
pTempo = 0 # tempo presente
cap = cv2.VideoCapture(0)
detector = mrm.deteccaoMao()

while True:
    success, img = cap.read()
    # Invertendo a imagem
    img = cv2.flip(img, 1)
    img = detector.encontreMaos(img) #, desenhar=False)
    listaRefeencias = detector.encontreReferencias(img) #, desenhar=False)
    if len(listaRefeencias) !=0:
        print(listaRefeencias[4])

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