from datetime import datetime, timedelta

hoje = datetime.now()
um_dia = timedelta(days=1)

amanha = hoje + um_dia
ontem = hoje - um_dia
print(ontem)


prazo = datetime(2026, 7, 24)
hoje = datetime.now()

if hoje > prazo:
    print("Prazo vencido!")
else:
    print("Ainda está no prazo")


agora = datetime.now()
futuro = datetime(2026, 12, 25)
dias_restantes = futuro - agora

print(dias_restantes)