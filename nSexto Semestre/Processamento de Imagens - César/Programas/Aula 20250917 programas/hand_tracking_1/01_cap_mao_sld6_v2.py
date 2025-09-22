import cv2
import time
import sys
import importlib.util

# Configuração da captura de vídeo
cap = cv2.VideoCapture(0)

# Outra resolução comum é 1280x720
# Alterando a resolução da câmera para 640x480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
largura_atual = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
altura_atual = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Resolução atual da câmera: {int(largura_atual)}x{int(altura_atual)}")

# Verificar se o MediaPipe está instalado
mediapipe_spec = importlib.util.find_spec("mediapipe")
use_mediapipe = mediapipe_spec is not None

if use_mediapipe:
    import mediapipe as mp
    try:
        print(f"MediaPipe versão: {mp.__version__}")
    except:
        print("MediaPipe instalado, versão não disponível")
else:
    print("MediaPipe não está instalado. Executando apenas visualização de câmera.")
    
# Variáveis globais para controle do fluxo
mp_drawing = None
mp_hands = None
hands = None

# Inicializa o detector de mãos apenas se o MediaPipe estiver disponível
if use_mediapipe:
    try:
        # Tenta inicializar o MediaPipe Hands usando um método alternativo
        # Isso contorna o erro "hands is not a known attribute"
        import importlib
        mp_module = importlib.import_module('mediapipe')
        
        # Tenta acessar os módulos necessários via getattr para evitar erros de atributo
        solutions_module = getattr(mp_module, 'solutions', None)
        if solutions_module is not None:
            mp_hands = getattr(solutions_module, 'hands', None)
            mp_drawing = getattr(solutions_module, 'drawing_utils', None)
            
            if mp_hands is not None:
                # Configurando o detector de mãos
                hands = mp_hands.Hands(
                    static_image_mode=False,
                    max_num_hands=2,
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5
                )
                print("MediaPipe Hands inicializado com sucesso")
            else:
                print("Módulo 'hands' não encontrado em mediapipe.solutions")
                use_mediapipe = False
        else:
            print("Módulo 'solutions' não encontrado em mediapipe")
            use_mediapipe = False
    except Exception as e:
        print(f"Erro ao inicializar MediaPipe Hands: {e}")
        use_mediapipe = False
        hands = None
else:
    print("Executando sem detecção de mãos")

# Loop principal
while True:
    # Captura frame da câmera
    success, img = cap.read()
    
    if not success:
        print("Falha ao capturar frame")
        break
    
    # Inverter a imagem ANTES do processamento para que as landmarks correspondam à imagem exibida
    img = cv2.flip(img, 1)
    
    # Processa o frame com MediaPipe Hands se disponível
    hand_landmarks = None
    if use_mediapipe and hands is not None:
        try:
            # Converte a imagem para RGB (MediaPipe usa RGB)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Processa a imagem já invertida
            results = hands.process(imgRGB)
            
            # Verifica se há landmarks de mão detectados
            if results.multi_hand_landmarks:
                print("Mão detectada!")
                hand_landmarks = results.multi_hand_landmarks
        except Exception as e:
            print(f"Erro ao processar frame: {e}")
    
    # Desenhar landmarks de mãos, se detectadas e o módulo drawing_utils estiver disponível
    if hand_landmarks and mp_drawing is not None:
        try:
            for hand_landmark in hand_landmarks:
                # Desenha os landmarks (pontos) da mão
                mp_drawing.draw_landmarks(
                    img,
                    hand_landmark,
                    mp_hands.HAND_CONNECTIONS if mp_hands else None,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
                )
        except Exception as e:
            print(f"Erro ao desenhar landmarks: {e}")
    
    # Obter a resolução atual e exibi-la na imagem
    largura_atual = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    altura_atual = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    texto_resolucao = f"Resolucao: {int(largura_atual)}x{int(altura_atual)}"
    
    # Exibir status do MediaPipe na imagem
    status_text = "MediaPipe Ativo" if use_mediapipe and hands is not None else "MediaPipe Inativo"
    
    # Adicionar textos à imagem
    cv2.putText(img, texto_resolucao, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(img, status_text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255) if not use_mediapipe else (0, 255, 0), 2)
    cv2.putText(img, "Pressione 'q' para sair", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    # Exibir a imagem
    cv2.imshow("Camera", img)

    # Verificar teclas pressionadas
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
    # Verificar se a janela foi fechada
    if cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) <= 0:
        break

# Liberar recursos
try:
    cap.release()
    cv2.destroyAllWindows()
    print("Programa encerrado com sucesso")
except Exception as e:
    print(f"Erro ao encerrar programa: {e}")