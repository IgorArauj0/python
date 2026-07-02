from datetime import datetime

def gerar_assinatura(nome):
    agora = datetime.now()
    print(agora.strftime(f"Assinatura de {nome} gerada em {agora.day}/{agora.month}/{agora.year} às {agora.hour}:{agora.minute}:{agora.second}"))

# solicita o nome e chama a função para exibir a assinatura
nome = input("Digite seu nome: ")
gerar_assinatura(nome)
