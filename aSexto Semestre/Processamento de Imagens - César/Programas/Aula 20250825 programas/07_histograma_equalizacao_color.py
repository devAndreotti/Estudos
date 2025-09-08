import cv2
import matplotlib.pyplot as plt

# Carrega a imagem colorida
img = cv2.imread('fruta_contraste.jpg')

# Converte a imagem de BGR para YUV (luminância, U e V)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# Aplica a equalização de histograma no canal Y (luminância)
img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

# Converte a imagem de volta de YUV para BGR
img_equalized = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

# Exibe a imagem original e a imagem equalizada
plt.figure(figsize=(10, 5))

# Mostrar imagem original
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.axis('off')

# Mostrar imagem equalizada
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img_equalized, cv2.COLOR_BGR2RGB))
plt.title('Imagem Equalizada')
plt.axis('off')

plt.show()