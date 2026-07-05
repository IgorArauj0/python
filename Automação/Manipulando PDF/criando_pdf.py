from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=12)
pdf.cell(0, 10, text="Relatório de Vendas", new_x='LMARGIN', new_y='NEXT')

pdf.ln(10)  # Adiciona uma linha em branco

pdf.set_font("Arial", size=10)
pdf.cell(0, 5, text="Eu sou um texto de **exemplo**", new_x='LMARGIN', new_y='NEXT', markdown=True)
pdf.ln(5)  # Adiciona uma linha em branco



pdf.multi_cell(0, 5, text="loren ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum loren ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum loren ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum", new_x='LMARGIN', new_y='NEXT')

pdf.ln(5)  # Adiciona uma linha em branco

pdf.image("net.jpeg", x='CENTER', y=pdf.get_y(), w=30)  # Adiciona a imagem no canto superior esquerdo

pdf.output("PDFNOVO.pdf")