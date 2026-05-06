#usando o if e else para criar um jogo de adivinhação simples
numero_secreto = 7
chute = int(input("Digite um número entre 1 e 10: "))

if chute == numero_secreto:
    print("Parabéns! Você acertou o número secreto!")
else: print("Ops! Você errou. Tente novamente!")