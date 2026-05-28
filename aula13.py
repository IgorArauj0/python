
#calculadora de descontos
#Os descontos são aplicados com base no valor da compra, seguindo as seguintes regras:
#Compras acima de R$ 1000,00 recebem um desconto de 20% de desconto.
#Compras entre R$ 500,00 e R$ 1000,00 recebem um desconto de 10% de desconto.
#Compras abaixo de R$ 500,00 não recebem desconto.

valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra > 1000:
    desconto = valor_compra * 0.20
    valor_final = valor_compra - desconto
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor final da compra: R$ {valor_final:.2f}")

elif valor_compra >= 500:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor final da compra: R$ {valor_final:.2f}")

else:
    print("Nenhum desconto aplicado.")
    print(f"Valor final da compra: R$ {valor_compra:.2f}")
