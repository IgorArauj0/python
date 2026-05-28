#and E
numero1 = 50
numero2 = 21
numero3 = 200

if numero1  > numero2 and numero3 > numero1:
    print("As duas condições são verdadeiras")


#excelente: 90-100
#bom: 80-89
#regular: 60-79
#ruim: 0-59 

nota = int(input("Digite a nota do aluno:(0-100 ) "))

if nota >= 90 and nota <= 100:
    print("Excelente")
elif nota >= 80 and nota <= 89:
    print("Bom")
elif nota >= 60 and nota <= 79:
    print("Regular")
else:
    print("Ruim")