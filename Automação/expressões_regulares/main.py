import re
import sys


# texto = "Eu tenho um gato"
# expressao = 'gato'

# resultado = re.search(expressao, texto)

# if resultado:
#     print(resultado.group())
# else:
#     print("A palavra não foi encontrada.")

# texto = "meu número de telefone é 123-456-7890 e do meu amigo é 987-654-3210"
# expressao = r"\d{3}-\d{3}-\d{4}"

# resultados = re.findall(expressao, texto)
# if resultados:
#     print("Números de telefone encontrados:")
#     for resultado in resultados:
#         print(resultado)


# texto = "data de hoje: 28/07/2025...A data de ontem foi 27-07-2025"
# expressao = r"\d{2}[/-]\d{2}[/-]\d{4}"

# novo_texto = re.sub(expressao, "XX/XX/XXXX", texto)
# print(novo_texto)

texto = "Meu e-mail é igorAraujo@gmail.com O do meu amigo é joaoSilva@yahoo.com"
expressao = r"\w+@\w+\.\w+"

resultados = re.findall(expressao, texto)
if resultados:
    for resultado in resultados:
        print(resultado)