from pypdf import PdfReader
import re


def retornar_datas(texto:str):
    datas = []
    expressao = r"\d{2}/\d{2}/\d{4}"
    resultados = re.findall(expressao, texto)
    if resultados:
        for resultado in resultados:
            datas.append(resultado)
    return datas

vendas_relatorio = PdfReader("relatorio_de_vendas.pdf")
print(f"Número de páginas: {len(vendas_relatorio.pages)}")

texto_completo = ""
for pagina in vendas_relatorio.pages:
    texto_completo += pagina.extract_text()
print(retornar_datas(texto_completo))