import os

caminho_pasta = 'img'

# Lista todos os itens na pasta
itens = os.listdir(caminho_pasta)

# Filtra apenas os arquivos
lista_arquivos = [arquivo for arquivo in itens if os.path.isfile(os.path.join(caminho_pasta, arquivo))]

print(lista_arquivos)
