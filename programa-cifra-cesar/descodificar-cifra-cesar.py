def decifra_cesar(texto, chave):

    resultado = ""
    
    # Iterando sobre cada caractere do texto
    for char in texto:
        # Verificando se o caractere é uma letra maiúscula
        if char.isupper():
            # Aplicando a cifra de César inversa para letras maiúsculas
            resultado += chr((ord(char) - chave - 65) % 26 + 65)
        # Verificando se o caractere é uma letra minúscula
        elif char.islower():
            # Aplicando a cifra de César inversa para letras minúsculas
            resultado += chr((ord(char) - chave - 97) % 26 + 97)
        else:
            # Adicionando caracteres não alfabéticos sem alteração
            resultado += char
    
    return resultado

# Solicitando ao usuário o texto criptografado e a chave
texto_criptografado = input("Digite o texto criptografado: ")
chave = int(input("Digite a chave (número inteiro): "))

# Chamando a função para decifrar o texto
texto_decifrado = decifra_cesar(texto_criptografado, chave)

# Exibindo o texto criptografado e o texto decifrado
print("Texto criptografado: ", texto_criptografado)
print("Texto decifrado: ", texto_decifrado)
