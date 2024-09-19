def cifracesar(texto, chave):
    
    resultado = ""
    
    # Iterando sobre cada caractere do texto
    for char in texto:
        # Verificando se o caractere é uma letra maiúscula
        if char.isupper():
            # Aplicando a cifra de César para letras maiúsculas
            resultado += chr((ord(char) + chave - 65) % 26 + 65)
        # Verificando se o caractere é uma letra minúscula
        elif char.islower():
            # Aplicando a cifra de César para letras minúsculas
            resultado += chr((ord(char) + chave - 97) % 26 + 97)
        else:
            # Adicionando caracteres não alfabéticos sem alteração
            resultado += char
    
    return resultado

# Solicitando ao usuário o texto e a chave
texto = input("Digite o texto a ser criptografado: ")
chave = int(input("Digite a chave (número inteiro): "))

# Chamando a função para criptografar o texto
textoCrip = cifracesar(texto, chave)

# Exibindo o texto original e o texto criptografado
print("Texto original: ", texto)
print("Texto criptografado: ", textoCrip)
