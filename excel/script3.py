from openpyxl import Workbook

print("Iniciando nosso rôbo...")
print("Lendo dados do arquivo de texto...")
file_txt = open("gastos.txt", "r", encoding="utf-8")

#Ler do arquivo
arquivo = file_txt.read()

lista_dados = arquivo.splitlines()

for i in range(len(lista_dados)):
    lista_dados[i] = lista_dados[i].split(",")
print(lista_dados)

#Criando arquivo excel
wb = Workbook()
ws = wb.active()

for row in lista_dados:
    ws.append(row)

ws.save('gastos.xlsx')
