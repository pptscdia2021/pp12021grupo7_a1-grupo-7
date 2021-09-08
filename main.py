import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd

url_page = 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'

page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

table = soup.find("table", {'id': 'ctl00_Contenido_tblÍndices'})
name = ""
porcent = ""
nroFila = 0

for fila in table.find_all("tr"):
    #for row in  tabla.find_all("td")::
    nroCelda=0
    for celda in fila.find_all('td'):
        if nroCelda==0:
            name=celda.text
            print("Nombre:", name)
        if nroCelda==3:
            porcent=celda.text
            print("Porcentaje de Dif:", porcent)
        nroCelda+=1
    nroFila+=1

    with open('bolsa_ibex35.csv', 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, porcent])
    csv_file.close()

with open('bolsa_ibex35.csv', 'r', encoding='utf-8') as csv_file2:
    csv_reader = csv.reader(csv_file2)
    next(csv_reader)
    for line in csv_reader:
        print(line)
csv_file2.close()
df = pd.read_csv('bolsa_ibex35.csv')

headerList= ["Name" , "Porcentaje"]

df.to_csv('bolsa_ibex35.csv',header=headerList, index=False)
if __name__ == "__main__":
    print("Principal")