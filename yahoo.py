# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:33:41 2021

@author: Oscar Ferreira
"""

# Importamos la libereia yFinance
import yfinance as yf


def yahoo(nonbreaccion):  # Definimos la funcion Yahoo, el parametro es el nombre da la accion a consultar

    # buscamos la accion
    tipo = yf.Ticker(nonbreaccion)
    # guardamos el valor de Compra
    compra = "Compra = "+str(tipo.info["ask"])
    # guardamos el valor de Venta
    venta = "Venta ="+str(tipo.info["bid"])
    # guardamos el nombre de la accion
    nombre = tipo.info["longName"]
    # Devuelve el nombre de la accion, el valor de compra y venta
    return nombre, compra, venta

    print(TEF.MC)
