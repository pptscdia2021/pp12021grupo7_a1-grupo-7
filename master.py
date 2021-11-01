"""
Created on Mon Oct  4 17:28:20 2021

@author: Oscar FERREIRA
"""

from yahoo.py import yahoo
from ibex.py import obtener_Datos


print("-------------MENU------------------")
print("1 - leer bolsa madrid CSV")
print("2 - Ingresae una URL para hacer Sripping")
print("3 - Consultar por una accion particular Con Yahoo")
print("4 - ver Dataset de Acciones descargado")
print("5 - Ver comparativa de acciones")
print("6 - Ver reporte")
print("")
print("0 - Salir")

rta=99
while rta!=0:
    rta=int(input("Ingrese opccion - "))
    if rta!=0:
        if rta==1:
            url="https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000&punto=indice"
            id_table="ctl00_Contenido_tblAcciones"
            obtener_Datos(url,id_table)
        elif rta==2:
           url=input("Ingresar URL para Web Sripping")
           it_table=input("ingresar ID_Table de la URL")
           obtener_Datos(url,id_table)
        elif rta==3:
            print("Opcion 3")
        elif rta==4:
            print("Opcion 4")
        elif rta==5:
            print("Opcion 5")
        elif rta==6:
            print("Opcion 6")
    else:
        print("Muchas gracias !!!!")
