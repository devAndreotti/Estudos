import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('folha_colorida.jpg', -1)
cv2.imshow('Folha Colorida',img)

color = ('b','g','r')
for channel,col in enumerate(color):
    histr = cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color = col, label=color[channel])
    plt.xlim([0,256])
plt.title('Histograma')
plt.xlabel("Intensidade")
plt.ylabel("QTD")
plt.text(50, 6000, "folha_colorida.jpg")
plt.xlim(0,255)
plt.grid(True)
plt.legend()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()