import matplotlib

#Identificar las 2 cotizaciones de mayor ganancia y de mayor perdida.


#df = df.sort_values([info_header], ascending=True)     Codigo para tener la tabla antes hecha ordenada

import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd

import os

url_page = "https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000&punto=indice"
id_table = "ctl00_Contenido_tblAcciones"
path = 'bolsa_ibex35.csv'


def obtener_Datos(url=url_page, table_id=id_table, file_csv=path, info_ob=2, info_header = "Porcentaje"):
    """Función que obtiene los datos de la tabla de una página. Parametros:
    url= Indica el url de la página
    table_id= id en el codigo HTML de la tabla
    file_csv= Path en donde va a localizar el archivo.csv con la data
    info_ob= número de la celda del dato que quiere sacar (aparte del label Name que se encontrará en la celda 0)
    info_header= Nombre que le pondrá como header al dato"""
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")

    table = soup.find("table", {'id': table_id })
    name = ""
    ultim = ""
    info = ""
    nroFila = 0

    fileName = r"{}".format(file_csv)   
    if os.path.exists(fileName):   #Verifico la existencia del archivo, en tal caso lo borra para reescribirlo
        os.remove(fileName)
    else:
        pass

    for fila in table.find_all("tr"):    #Itera sobre cada Fila
        nroCelda=0
        for celda in fila.find_all('td'): #En cada fila itera sobre cada celda
            if nroCelda==0:
                name=celda.text      #Si la celda es la primera, le asigna ese valor a 'name' ya que la primera fila suele ser el nombre
            if nroCelda == 1:
                ultim = celda.text
            if nroCelda== info_ob:    #Si el num de celda concide con info_ob le asigna ese valor a 'info'
                info=celda.text
            nroCelda+=1
        nroFila+=1

        with open(file_csv, 'a', newline='', encoding='utf-8') as csv_file:   
            writer = csv.writer(csv_file)
            writer.writerow([name, ultim, info, datetime.now()])    #Abre el archivo y escribe cada fila en forma de list para que el archivo csv lo detecte
        csv_file.close()

    df = pd.read_csv(file_csv)     #Con la libreria pandas guardo el archivo en formato de Tabla
    headerList= ["Name" , "Ultimo", info_header, "Fecha"]  
    df.columns = headerList
    df.to_csv(file_csv, index=False)    #Le agrego un header con pandas

    #df = df.sort_values([info_header], ascending=True)     Codigo para tener la tabla antes hecha ordenada
    return df

if __name__ == "__main__":
    print("Principal")

lista_porcentajes = list(obtener_Datos().sort_values(["Porcentaje"], ascending=True).Porcentaje)
print(list(obtener_Datos().sort_values(["Porcentaje"], ascending=True).Porcentaje))

negativos=[]

for i in range(len(lista_porcentajes)):
    if "-" in  (lista_porcentajes[i]):
        negativos.append(lista_porcentajes[i])
    else:
        pass
        
print(lista_porcentajes)
print(negativos)


