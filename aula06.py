#Números Randomicos
# Ele serve para gerar números aleatórios, o que é útil em várias situações, como jogos, simulações, etc.
import random

print(random.randrange(1, 101)) # gera um número inteiro aleatório entre 1 e 100

print(random.random()) # gera um número flutuante aleatório entre 0.0 e 1.0

print(random.randint(10, 20)) # gera um número inteiro aleatório entre 10 e 20, incluindo ambos os extremos.

frutas = ["maçã", "banana", "laranja", "uva", "pera"]
print(random.choice(frutas)) # seleciona aleatoriamente um elemento da lista frutas


numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros) # embaralha a lista numeros
print(numeros) # exibe a lista embaralhada


print(random.uniform(1.5, 3.5)) # gera um número flutuante aleatório entre 1.5 e 3.5   
