# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:33:41 2021

@author: Oscar Ferreira
"""

import yfinance as yf                                                          # Importamos la libereia yFinance

def yahoo (nonbreaccion):                                                      #Definimos la funcion Yahoo, el parametro es el nombre da la accion a consultar
     
    tipo= yf.Ticker(nonbreaccion)                                              # buscamos la accion
    compra="Compra = "+str(tipo.info["ask"])                                   # guardamos el valor de Compra
    venta="Venta ="+str(tipo.info["bid"])                                      # guardamos el valor de Venta
    nombre=tipo.info["longName"]                                               # guardamos el nombre de la accion                                                        
    return nombre, compra, venta                                               # Devuelve el nombre de la accion, el valor de compra y venta
    
    
    


