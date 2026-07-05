import re

# texto = "Código: PROD-12343, PROD-56784, PROD-90124"
# expressao = r"\w{4}-(\d{5})"

# resultado = re.search(expressao, texto)
# if resultado:
#     print(resultado.group(1))

texto = "Meu e-mail é igorAraujo@gmail.com"
expressao = r"(\w+)@(\w+)\.(\w+)"
resultado = re.search(expressao, texto)
if resultado:
    print(f"Usuário: {resultado.group(0)}")
    print(f"Usuário: {resultado.group(1)}")
    print(f"Domínio: {resultado.group(2)}")
    print(f"Extensão: {resultado.group(3)}")