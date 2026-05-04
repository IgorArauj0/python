nome = input("Digite seu nome: ")

print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

# Podemos usar a função input() para receber dados do usuário. O valor retornado por input() é sempre uma string.

nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"{nome}, sua média é: {media}")