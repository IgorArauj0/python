from datetime import datetime

# pega data e hora atual
data_atual = datetime.now()
# extrai a hora atual
hora = data_atual.hour

# escolhe a saudação conforme o horário
if hora < 12 and hora >= 6:
    print("Bom dia!")
elif hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")

# mostra a hora atual
print(f"Agora são {hora} horas.")