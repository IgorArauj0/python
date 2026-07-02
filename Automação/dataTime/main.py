from datetime import datetime

# data/hora atual
agora = datetime.now()

# componentes
print(agora.day)      # dia
print(agora.month)    # mês
print(agora.year)     # ano
print(agora.hour)     # hora
print(agora.minute)   # minuto
print(agora.second)   # segundo

# frase resumida
print(f"Hoje é dia {agora.day} do mês {agora.month} do ano de {agora.year}.")

# data formatada com strftime: converte a data para uma string no formato DD/MM/AAAA HH:MM:SS
print(agora.strftime("%d/%m/%Y %H:%M:%S"))

# data fixa
aniversario = datetime(1999, 11, 2)
print(aniversario)


