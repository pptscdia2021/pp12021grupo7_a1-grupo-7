import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup

url_page = 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'

page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

table = soup.find("table", {'id': 'ctl00_Contenido_tblÍndices'})
name = ""
price = ""
nroFila = 0

for fila in table.find_all("tr"):
    #for row in  tabla.find_all("td")::
    nroCelda=0
    for celda in fila.find_all('td'):
        if nroCelda==0:
            name=celda.text
            print("Nombre:", name)
        if nroCelda==4:
            price=celda.text
            print("Maximo:", price)
        if nroCelda == 5:
            price2=celda.text
            print("Minimo:", price2)
        nroCelda+=1
    nroFila=nroFila+1


if __name__ == "__main__":
    print("Principal")