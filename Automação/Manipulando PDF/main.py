from pypdf import PdfReader

relatorio = PdfReader("relatorio_de_vendas.pdf")

# pagina_1 = relatorio.pages[0]

# texto = pagina_1.extract_text()
# print(texto)
# relatorio.close()

for pagina in relatorio.pages:
    print(pagina.extract_text())