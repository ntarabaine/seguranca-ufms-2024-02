# Importando bibliotecas
from PIL import Image

# Converte uma string binária para texto usando codificação ASCII
def binarioParaTexto(binStr):
    retStr = ''
    for i in range(0, len(binStr) // 8):
        retStr += chr(int(binStr[i*8:i*8+8], 2))
    return retStr

# Obtendo entrada do usuário para encontrar qual arquivo abrir
print('Digite o arquivo de imagem para decodificar:')
imgEntrada = input()
print('Digite o número de caracteres a decodificar:')
numCaracteres = int(input())
numBits = numCaracteres * 8

# Carregando os dados dos pixels da imagem
imagem_pre = Image.open(imgEntrada)
largura, altura = imagem_pre.size
pixels = imagem_pre.load()

# Encontrando o bit menos significativo de cada pixel
binStr = ''
bitAtual = 0
for x in range(0, largura):
    if bitAtual >= numBits:
        break

    # Pegando o pixel atual
    pixelAtual = pixels[x, 0]

    # Mudando os valores de r, g e b do pixel
    for c in range(0, 3):
        if bitAtual >= numBits:
            break
        corBin = list(format(pixelAtual[c], 'b').zfill(8))
        binStr += corBin[7]

        bitAtual += 1

# Interpretando os bits para obter o texto ASCII
print(binarioParaTexto(binStr))
print()
