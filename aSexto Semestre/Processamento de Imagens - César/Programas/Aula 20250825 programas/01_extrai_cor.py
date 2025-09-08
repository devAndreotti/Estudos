import cv2

#
# Extrai a cor do pixel na L,C=150
#

imagem1 = cv2.imread("frutas.jpg")
valorPixel1 = imagem1[150,150]
print("Cor Pixel BGR (150,150):",valorPixel1)
print("Dados Img:", imagem1.shape)
print("Tamanho Imagem:", imagem1.size)

# #
# # Convertendo Imagem Tons de Cinza na L,C=150
# #

imagem2 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
valorPixel2 = imagem2[150,150]
print("Imagem Tom Cinza. Valor Pixel (150,150):",valorPixel2)


# #
# # Importando Imagem Colorida diretamente
# # em Tons de Cinza e apresentando os valores para L,C=150
# #

imagem1a = cv2.imread("frutas.jpg",cv2.IMREAD_GRAYSCALE)
valorPixel1a = imagem1a[150,150]
print("Imagem Importada em Tom Cinza. Valor Pixel (150,150):",valorPixel1a)
print("Dados Img:", imagem1a.shape)


# #
# # Imagem Original Tons de Cinza na L,C=150
# #

# imagem3 = cv2.imread("campo_tom_cinza.jpg")
# valorPixel3 = imagem3[150,150]
# print("Imagem Original Tons Cinza. Valor Pixel (150,150):",valorPixel3)

# imagem4 = cv2.cvtColor(imagem3, cv2.COLOR_RGB2GRAY)
# valorPixel4 = imagem4[150,150]
# print("Imagem Original Tons Cinza CONV. Valor Pixel (150,150):",valorPixel4)


# #
# # Lendo cada um dos canais de cor na L,C=150
# #

print("Canais RGB pixel (150, 150):",valorPixel1)
valorR = imagem1[150, 150, 2]
valorG = imagem1[150, 150, 1]
valorB = imagem1[150, 150, 0]
print("Canal R pixel (150, 150):",valorR)
print("Canal G pixel (150, 150):",valorG)
print("Canal B pixel (150, 150):",valorB)

#
# Alterando o valor do pixel na L,C=150
#

print("Valor Pixel (150, 150):", imagem1[150,150])
imagem1[150,150] = [255, 255, 255]
print("Valor Alterado Pixel (150, 150):", imagem1[150,150])