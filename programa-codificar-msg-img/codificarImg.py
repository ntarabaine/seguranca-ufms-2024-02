# Importando bibliotecas
from PIL import Image

# Converte uma string para binário usando codificação ASCII
def textoParaBinario(texto):
    return ''.join((format(ord(i), 'b')).zfill(8) for i in texto)

# Obtendo entrada do usuário para encontrar qual arquivo abrir
print('Digite o arquivo de imagem para abrir:')
imgEntrada = input()
print('Digite o texto para codificar:')
textoEntrada = input()
print('Digite o arquivo de imagem para salvar:')
imgSaida = input()

# Pegando a nossa mensagem e convertendo para binário
mensagemBin = textoParaBinario(textoEntrada)

# Carregando os dados dos pixels da imagem
imagem_pre = Image.open(imgEntrada)
largura, altura = imagem_pre.size
pixels = imagem_pre.load()

# Mudando o bit menos significativo de cada pixel para corresponder a cada bit da nossa mensagem codificada
bitAtual = 0
for x in range(0, largura):
    if bitAtual >= len(mensagemBin):
        break

    # Pegando o pixel atual
    pixelAtual = pixels[x, 0]
    #print('[%d, %d]: [%d, %d, %d]' % (x, 0, pixelAtual[0], pixelAtual[1], pixelAtual[2]))

    # Mudando os valores de r, g e b do pixel
    novoPixel = list(pixelAtual)
    for c in range(0, 3):
        if bitAtual >= len(mensagemBin):
            break
        corBin = list(format(pixelAtual[c], 'b').zfill(8))
        corBin[7] = mensagemBin[bitAtual]
        corBin = ''.join(corBin)
        novoPixel[c] = int(corBin, 2)

        bitAtual += 1

    # Substituindo o pixel antigo
    pixelAtual = tuple(novoPixel)
    pixels[x, 0] = pixelAtual

# Reescrevendo os dados dos pixels da imagem em uma nova imagem
imagem_pre.save(imgSaida)
