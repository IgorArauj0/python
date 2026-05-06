#Trabalhando com Strings

#Imprimindo posição de letras em uma string
posicaoLetra = "Python"
print(posicaoLetra[0]) #P
print(posicaoLetra[1]) #y
print(posicaoLetra[2]) #t
print(posicaoLetra[3]) #h
print(posicaoLetra[4]) #o
print(posicaoLetra[5]) #n   


frase = "Olá, Programadores!"
parte = frase[1:19] #Programadores
print(parte)

primeiros = frase[:5] #Olá,
print(primeiros)

ultimos = frase[-6:] #Programadores!
print(ultimos)


frase2 = "Python é uma linguagem de programação incrível!"
print("python" in frase2) # False, pois a comparação é case-sensitive
print("Python" in frase2) # True


#Verifica se a palavra "Python" está presente na mensagem
mensagemPython = "Python é uma linguagem de programação incrível!"
if "Python" in mensagemPython:
    print("A palavra 'Python' está presente na mensagem.")


#usado para remover espaços em branco no início e no fim de uma string
espacoTexto = "   Teste, com espaços extras!   "
print(espacoTexto.strip()) # Remove os espaços em branco do início e do fim da string


#split() é usado para dividir uma string em uma lista de substrings com base em um delimitador especificado (por padrão, é um espaço em branco).
frase3 = "Python é uma linguagem de programação incrível!"
palavras = frase3.split() # Divide a frase em palavras usando o espaço como delimitador
print(palavras) # ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'incrível!']


#Cortando os asteriscos do início e do fim da string usando strip()
texto = "*******Python!*******"
print(texto.strip("*")) # Remove os asteriscos do início e do fim da string