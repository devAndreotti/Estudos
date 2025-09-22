import cv2
import mediapipe as mp 
import time

# Inicializa a captura de vídeo
cap = cv2.VideoCapture(0)

# Define a resolução da captura (largura e altura)
# Valores comuns: 640x480, 1280x720, 1920x1080
largura = 640
altura = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, largura)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, altura)

# Verifica a resolução efetiva (algumas webcams podem não suportar a resolução solicitada)
largura_atual = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
altura_atual = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"Resolução configurada: {largura_atual}x{altura_atual}")

# Função para mudar a resolução durante a execução (você pode chamá-la pressionando teclas)
def mudar_resolucao(cap, largura, altura):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, largura)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, altura)
    largura_atual = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    altura_atual = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"Nova resolução: {largura_atual}x{altura_atual}")
    return largura_atual, altura_atual

# Imprimindo a versão do mediapipe
# print("\n\n\nA versão do mediapipe é:", mp.__version__, "\n\n\n")

# A versão original do mediapipe é: 0.10.14

#
# Importa API
#
mpMaos = mp.solutions.hands

#
# Criando objeto mao
#

# class Hands(static_image_mode=False,
#             max_num_hands=2,
#             model_complexity=1,
#             min_detection_confidence=0.5,
#             min_tracking_confidence=0.5)

# static_image_mode: Se a entrada for uma imagem única, definimos como true, caso contrário, configuramos false para rastrear quadros
# max_num_hands: número máximo de mãos no quadro, padrão 2
# model_complexity: Dois modelos 0 ou 1 onde 1 fornece melhores resultados que 0
# min_detection_confidence: confiança das detecções
# min_tracking_confidence: se rastreando quadros, rastreando a confiança


maos = mpMaos.Hands()

while True:
    # Verifica se a câmera foi aberta com sucesso
    if not cap.isOpened():
        print("Erro: Não foi possível acessar a webcam. Tentando reconectar...")
        cap.release()
        time.sleep(1)
        cap = cv2.VideoCapture(0)
        continue
    
    # Lê o próximo frame da webcam
    success, img = cap.read()
    
    # Verifica se a leitura foi bem-sucedida
    if not success or img is None:
        print("Aviso: Falha ao ler frame da webcam. Tentando novamente...")
        continue
    
    # Tenta converter para RGB e processar com MediaPipe
    try:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resultado = maos.process(imgRGB)
    
        if resultado.multi_hand_landmarks:
            print(resultado.multi_hand_landmarks)
    except cv2.error as e:
        print(f"Erro ao processar frame: {e}")
        continue

    try:
        # Inverter para mostrar a imagem correta
        img = cv2.flip(img, 1)
        
        # Adiciona informações sobre a resolução atual na imagem
        largura_atual = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        altura_atual = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        texto_resolucao = f"Resolucao: {int(largura_atual)}x{int(altura_atual)}"
        cv2.putText(img, texto_resolucao, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Adiciona instruções na tela
        cv2.putText(img, "1: 640x480 | 2: 1280x720 | 3: 1920x1080 | q: Sair", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow("Camera", img)
    except Exception as e:
        print(f"Erro ao exibir imagem: {e}")
        continue

    # Captura tecla pressionada
    key = cv2.waitKey(1)
    
    # Alterar resolução com base nas teclas pressionadas
    try:
        if key == ord('1'):
            mudar_resolucao(cap, 640, 480)
            # Liberar e reabrir a câmera após mudança de resolução para evitar erros
            cap.release()
            time.sleep(0.5)
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        elif key == ord('2'):
            mudar_resolucao(cap, 1280, 720)
            cap.release()
            time.sleep(0.5)
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        elif key == ord('3'):
            mudar_resolucao(cap, 1920, 1080)
            cap.release()
            time.sleep(0.5)
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        elif key == ord('q'):
            break
    except Exception as e:
        print(f"Erro ao mudar resolução: {e}")
    
    # Verifica se a janela foi fechada
    try:
        if cv2.getWindowProperty('Camera',cv2.WND_PROP_VISIBLE) <= 0:
            break
    except:
        break
# Libera recursos adequadamente
print("Encerrando o programa...")
try:
    cap.release()
    cv2.destroyAllWindows()
except:
    pass