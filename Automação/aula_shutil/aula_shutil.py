import shutil 
from pathlib import Path

# shutil.copy2('arquivinho.txt', "backup/arquivinho_copiado.txt")

# shutil.copytree("meus_arquivos", "meus_arquivos_copiados", dirs_exist_ok=True)

# shutil.move("meus_arquivos/arquivo_teste.txt", "meus_arquivos/arquivo_teste_movido.txt")

# shutil.rmtree("meus_arquivos_copiados")

# shutil.make_archive("meus_arquivos", "zip", "meus_arquivos")

# shutil.unpack_archive("meus_arquivos.zip", "meus_arquivos_descompactados", "zip") 


arquivo = Path("arquivos")
arquivos_backup = Path("arquivos_backup")

if not arquivos_backup.exists():
    arquivos_backup.mkdir()

shutil.copytree("arquivos", arquivos_backup, dirs_exist_ok=True)

