if __name__ == '__main__':
    print("Cotizaciones") 

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#Identificar las 2 cotizaciones de mayor ganancia y de mayor perdida.

#si los cotizaciones están en una lista:

class bolsa_valores:
    def __init__(self, nombre , max_ganancia , min_ganancia):
        self.nombre = nombre
        self.max_ganancia = max_ganancia
        self.min_ganancia = min_ganancia


