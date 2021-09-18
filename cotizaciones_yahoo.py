import yfinance as yf


#nombres=[ "AMZN", "CL=F", "^RUT", "BTC-USD"]  
#tipo="perdida" - "ganancia"
#inicio="2021-09-03"                                  
#final="2021-09-04"
 
# #MODO DE EJEMPLO DE COMO LLAMAR A LA FUNCIÓN: cotizaciones_yf("ganancia","2021-09-03","2021-09-04",[ "AMZN", "CL=F", "^RUT", "BTC-USD"] ):


nombre_cotizaciones=[]
valor_cotizaciones=[]
nombres_ordenados=[]
nombre_cotizaciones=[]


def cotizaciones_yf(tipo,inicio,final,nombres):
    for i in range(len(nombres)):
        df = yf.download(nombres[i], start=inicio, end=final,group_by="ticker")
        open= list(df["Open"])[0]                                                       #Obtengo los Opens
        close = list(df["Close"])[0]                                                    #Obtengos los Closes

        if open < close:
            nombre_cotizaciones.append(nombres[i])
            valor_cotizaciones.append((close/open))                 
        elif open > close:                                                              #Calculo del valor respectivo
            nombre_cotizaciones.append(nombres[i])
            valor_cotizaciones.append(((close/open)-1))
        else:
            nombre_cotizaciones.append(nombres[i])
            valor_cotizaciones.append(0)
    valor_ordenado= valor_cotizaciones.copy()
    valor_ordenado.sort()                                                              #Ordeno valores
    a=0

    for f in range(len(nombres)):
        if valor_ordenado[0]==valor_cotizaciones[f]:
            nombres_ordenados.append(nombre_cotizaciones[f])
        else:
            pass
    for r in range(len(nombres)):
        if valor_ordenado[1]==valor_cotizaciones[r]:
            nombres_ordenados.append(nombre_cotizaciones[r])
        else:
            pass                                                           #Ordeno Nombres, cada index del valor ordenado, corresponde al index del nombre correspondiente
    for a in range(len(nombres)):
        if valor_ordenado[2]==valor_cotizaciones[a]:
            nombres_ordenados.append(nombre_cotizaciones[a])
        else:
            pass
    for n in range(len(nombres)):
        if valor_ordenado[3]==valor_cotizaciones[n]:
            nombres_ordenados.append(nombre_cotizaciones[n])
        else:
            pass

                



    if tipo == "perdida":
        if valor_ordenado[0]> 0:
            #print("No hay cotizaciones con pérdida")
            devolver = []
            return devolver
        elif valor_ordenado[1]>0:
            #print("La cotización con mayor pérdida es: \n" + str(nombres_ordenados[0]) , "con una valor de " + str(valor_ordenado[0]))
            devolver = [{"Nombre":nombres_ordenados[0], "Valor":valor_ordenado[0]}]
            return devolver
        else:
            #print("Las cotizaciones con mayor pérdida son: \n" + str(nombres_ordenados[0]) , " con una valor de: ", str(valor_ordenados[0]), "\n " , str(nombres_ordenados[1]) , " con una valor de: ", str(valor_ordenado[1]))
            devolver = [{"Nombre":nombres_ordenados[0], "Valor":valor_ordenado[0]},{"Nombre":nombres_ordenados[1], "Valor":valor_ordenado[1]}]
            return devolver
    if tipo == "ganancia":
        if valor_ordenado[-1]< 0:
            devolver = []
            return devolver
        elif valor_ordenado[-2] <0:
            #print("La cotización con mayor ganancia es \n" + str(nombres_ordenados[-1]) , "con una valor de " + str(valor_ordenado[-1]))
            devolver = [{"Nombre":nombres_ordenados[-1], "Valor":valor_ordenado[-1]}]
            return devolver
        else:
            #print("Las cotizaciones con mayor pérdida son: \n" + str(nombres_ordenados[-2]) , " con una valor de: ", str(valor_ordenado[-2]), "\n " , str(nombres_ordenados[-1]) , " con una valor de: ", str(valor:ordenado[-1]) )
            devolver =[{"Nombre":nombres_ordenados[-1], "Valor":valor_ordenado[-1]},{"Nombre":nombres_ordenados[-2], "Valor":valor_ordenado[-2]}]
            return devolver



