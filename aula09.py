#função if 
numero1 = 30
numero2 = 20    
#Se numero1 for maior que numero2, imprima a mensagem
if numero1 > numero2:
    print("numero1 é maior que numero2")


#python função if...elif
nota = 7
nota2 = 8
if nota >= nota2:
    print("Parabéns! Você passou!")
    #elif é usado para verificar uma condição adicional se a primeira condição for falsa
elif nota >= 5:
    print("Você está na média, mas pode melhorar.")