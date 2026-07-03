
import random

# numero_inteiro = random.randint(1, 100)
# print(numero_inteiro)

# float_aleatorio = random.uniform(1, 20)
# print(float_aleatorio)

# cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# # cartas_aleatorias = random.choices(cartas, k=2)
# cartas_aleatorias = random.sample(cartas, k=2)

# print(f"As cartas escolhidas são: {cartas_aleatorias}")


musicas = ['Imagine', 'Bohemian Rhapsody', 'Stairway to Heaven', 'Hotel California', 'Sweet Child O\' Mine']
random.shuffle(musicas)
print(f"A ordem aleatória das músicas é: {musicas}")