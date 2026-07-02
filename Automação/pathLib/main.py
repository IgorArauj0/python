#gerenciamento de arquivos
from pathlib import Path

# caminho = Path("arquivinho.txt")
# caminho_absoluto = Path(r"C:\Users\Luciana\Documents\python-exemplo\arquivinho2.txt")

# print(caminho_absoluto)

# caminho = Path("arquivinho.txt")
# if caminho.exists():
#    print("Existe!")
# else:
#    print("Não existe")

# caminho = Path("arquivinho.txt")

# if caminho.is_file():
#     print("É arquivo!")
# elif caminho.is_dir():
#     print("É uma pasta!")


# nova_pasta = Path("NovaPasta/outraPasta/maisUmaPasta")
# nova_pasta.mkdir(exist_ok=True, parents=True)

# arquivinho = Path("arquivinho.txt")

# novaPasta = Path("NovaPasta")

# arquivinho.unlink()
# novaPasta.rmdir()


# arquivinho = Path("arquivinho.txt")
# texto = arquivinho.read_text()
# print(texto)
# arquivinho.write_text("Olá, Galera!", encoding="utf-8")

pasta = Path("minha_pasta")
for arquivo in pasta.glob("*.pdf"):
    print(arquivo)


    


