# Trabalhando com strings pt 2

nome = "Alice"
idade = 25
altura = 1.68

# f = formatação de string, permite incluir variáveis diretamente dentro da string usando chaves {}
mensagem = f"Meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros."
print(mensagem)


texto = "Olá, Programadores!"

texto_upper = texto.upper() # Converte a string para maiúsculas
print(texto_upper) # OLÁ, PROGRAMADORES!

texto_lower = texto.lower() # Converte a string para minúsculas
print(texto_lower) # olá, programadores!

texto_capitalized = texto.capitalize() # Converte a primeira letra da string para maiúscula e o restante para minúscula
print(texto_capitalized) # Olá, programadores!

ocorrencia = texto.count("o") # Conta quantas vezes a letra "o" aparece na string
print(ocorrencia) # 2

texto_substituido = texto.replace("Programadores", "Desenvolvedores") # Substitui "Programadores" por "Desenvolvedores"
print(texto_substituido) # Olá, Desenvolvedores!    