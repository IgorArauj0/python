#Executar a idade do usuário para garantir a legilidade para votar
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você está apto a votar!")
else:
    print("Você não está apto a votar.")


numero1 = 2
numero2 = 6
if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}")
elif numero1 == numero2:
    print(f"{numero1} é igual a {numero2}")

else:
    print(f"{numero1} é menor que {numero2}")