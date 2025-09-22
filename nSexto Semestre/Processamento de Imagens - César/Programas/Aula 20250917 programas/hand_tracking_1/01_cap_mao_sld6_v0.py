import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)

# Outra resolução comum é 1280x720
# Alterando a resolução da câmera para 640x480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
largura_atual = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
altura_atual = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Resolução atual da câmera: {int(largura_atual)}x{int(altura_atual)}")
# Imprimindo a versão do mediapipe
# print("\n\n\nA versão do mediapipe é:", mp.__version__, "\n\n\n")

# A versão original do mediapipe é: 0.10.14

#
# Importa API
#
mpMaos = mp.solutions.hands

maos = mpMaos.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resultado = maos.process(imgRGB)

    if resultado.multi_hand_landmarks:
        print(resultado.multi_hand_landmarks)

    # Inverter para mostrar a imagem correta
    img = cv2.flip(img, 1)
    
    # Obter a resolução atual e exibi-la na imagem
    largura_atual = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    altura_atual = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    texto_resolucao = f"Resolucao: {int(largura_atual)}x{int(altura_atual)}"
    
    # Adicionar texto à imagem
    cv2.putText(img, texto_resolucao, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("Camera", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if cv2.getWindowProperty('Camera',cv2.WND_PROP_VISIBLE) <= 0:
        break
cv2.destroyAllWindows()