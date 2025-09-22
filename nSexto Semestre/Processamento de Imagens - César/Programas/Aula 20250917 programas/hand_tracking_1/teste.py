# STEP 1: Import the necessary modules.
import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Função simplificada para desenhar landmarks das mãos usando OpenCV
def draw_landmarks_on_image(rgb_image, detection_result):
    """
    Desenha os landmarks e conexões das mãos usando OpenCV.
    Esta implementação é compatível com todas as versões do MediaPipe.
    """
    hand_landmarks_list = detection_result.hand_landmarks
    annotated_image = np.copy(rgb_image)
    height, width, _ = annotated_image.shape
    
    # Definir as conexões entre os landmarks da mão
    connections = [
        # Polegar
        (0, 1), (1, 2), (2, 3), (3, 4),
        # Indicador
        (0, 5), (5, 6), (6, 7), (7, 8),
        # Médio
        (0, 9), (9, 10), (10, 11), (11, 12),
        # Anelar
        (0, 13), (13, 14), (14, 15), (15, 16),
        # Mínimo
        (0, 17), (17, 18), (18, 19), (19, 20),
        # Palma da mão (conexões base)
        (0, 17), (5, 9), (9, 13), (13, 17)
    ]
    
    # Desenhar cada mão detectada
    for landmarks in hand_landmarks_list:
        # Cores para visualização
        landmark_color = (0, 255, 0)  # Verde para pontos
        connection_color = (255, 0, 0)  # Azul para linhas
        
        # Desenhar cada ponto de referência (landmark)
        points = []
        for i, landmark in enumerate(landmarks):
            # Converter coordenadas normalizadas para pixels
            x = int(landmark.x * width)
            y = int(landmark.y * height)
            points.append((x, y))
            
            # Desenhar círculo em cada ponto de referência
            cv2.circle(annotated_image, (x, y), 5, landmark_color, -1)
            
            # Opcionalmente, adicionar número do landmark
            # cv2.putText(annotated_image, str(i), (x+10, y+10), 
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
        
        # Desenhar as conexões entre os pontos
        for connection in connections:
            start_idx, end_idx = connection
            if start_idx < len(points) and end_idx < len(points):
                cv2.line(annotated_image, points[start_idx], points[end_idx], 
                         connection_color, 2)
    
    return annotated_image

# STEP 2: Create an HandLandmarker object.
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

# STEP 3: Load the input image.
image = mp.Image.create_from_file("image.jpg")

# STEP 4: Detect hand landmarks from the input image.
detection_result = detector.detect(image)

# STEP 5: Process the classification result. In this case, visualize it.
annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
# Convertendo a imagem para formato BGR que o OpenCV espera
img_to_show = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
# Exibindo a imagem com cv2.imshow (padrão OpenCV)
cv2.imshow("Hand Landmarks", img_to_show)
# Aguardando pressionar uma tecla para fechar a janela
cv2.waitKey(0)
# Fechando todas as janelas
cv2.destroyAllWindows()