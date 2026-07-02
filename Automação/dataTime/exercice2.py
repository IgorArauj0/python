from datetime import datetime

# pega a data e hora atual
agora = datetime.now()
# extrai o mês atual
mes_atual = agora.month

# exibe o mês atual e quantos meses faltam para terminar o ano
print(f"Estamos no mês {mes_atual}. Restam {12 - mes_atual} meses para o final do ano.")