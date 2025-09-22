import cv2
import mediapipe as mp 
import time

# Classe para detecção de mãos
# Recebe como parâmetros:
# mode: modo de detecção
# mode = False: modo de detecção de vídeo
# nummaxMaos: número máximo de mãos a serem detectadas
# complexidade: complexidade do modelo
# certezadeteccao: certeza da detecção
# certezarastreamento: certeza do rastreamento
class deteccaoMao():
    def __init__(self, mode=False, nummaxMaos=4, complexidade =1, certezadeteccao=0.5, certezarastreamento=0.5 ):
        self.mode = mode
        self.numaxMaos = nummaxMaos
        self.complexidade = complexidade
        self.certezadeteccao = certezadeteccao
        self.certezarastreamento = certezarastreamento

#
# Importa API
#
        self.mpMaos = mp.solutions.hands
  
#
# Criando objeto mao
#

# class Hands(static_image_mode=False,
#             max_num_hands=2,
#             model_complexity=1,
#             min_detection_confidence=0.5,
#             min_tracking_confidence=0.5)

        self.maos = self.mpMaos.Hands(self.mode, self.numaxMaos, self.complexidade,
                                        self.certezarastreamento, self.certezadeteccao)
#
# Método para desenhar as referencias
#

        self.mpDraw = mp.solutions.drawing_utils

# Método para encontrar as mãos
# Recebe como parâmetros:
# img: imagem a ser analisada
# desenhar: se True desenha as mãos
    def encontreMaos(self, img, desenhar=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.resultado = self.maos.process(imgRGB)

        if self.resultado.multi_hand_landmarks:
             for maosLista in self.resultado.multi_hand_landmarks:
                if desenhar:
                    self.mpDraw.draw_landmarks(img, maosLista, self.mpMaos.HAND_CONNECTIONS)

        return img 

# Método para encontrar as referencias
# Recebe como parâmetros:
# img: imagem a ser analisada
# numMao: número da mão a ser analisada
# desenhar: se True desenha as referencias
    def encontreReferencias(self, img, numMao=0, desenhar = True):
        listaReferencias = []
        if self.resultado.multi_hand_landmarks:
            minhaMao = self.resultado.multi_hand_landmarks[numMao]
            for id, mr in enumerate(minhaMao.landmark):
                h, w, c = img.shape
                cx, cy = int(mr.x*w), int(mr.y*h)
                #print(id, cx, cy)
                listaReferencias.append([id, cx, cy])
                if desenhar:
                    #if id == 4:
                        cv2.circle(img, (cx, cy), 12, (55, 5, 255), cv2.FILLED)
        return listaReferencias


def main():
    aTempo = 0 # tempo anterior
    pTempo = 0 # tempo presente
    cap = cv2.VideoCapture(0)
    detector = deteccaoMao()
    
    while True:
        success, img = cap.read()
        img = detector.encontreMaos(img)
        listaRefeencias = detector.encontreReferencias(img)
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

if __name__ == "__main__":
    main()