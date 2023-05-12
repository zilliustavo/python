import PyPDF2
from openpyxl import Workbook

print("Iniciando nosso robô...")
pdf_file = open("gastos.pdf", "rb")

read_pdf = PyPDF2.PdfReader(pdf_file)

number_of_pages = read_pdf.pages

page = read_pdf.pages[0]
print("Lendo dados do arquivo PDF...")
page_content = page.extract_text()

print(page_content)

parsed = page_content.splitlines()

print(parsed)

parsed = page_content.split("   ")
while ' ' in parsed:
   parsed.remove(' ')

lista_dados = []
for i in range(0, len(parsed) - 3, 3):
    lista_dados.append([parsed[i], parsed[i+1],parsed[i+2]])

print("Criandoa arquivo .Xlsx")
wb = Workbook()
ws = wb.active

for row in lista_dados:
    ws.append(row)

wb.save(filename="gastos2.xlsx")

print("Leitura Finalizada!")