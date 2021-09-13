from web_scrapping import obtener_Datos
a= list(obtener_Datos().sort_values(["Porcentaje"], ascending=True).Porcentaje)
b= list(obtener_Datos().sort_values(["Porcentaje"], ascending=True).Name)

def cotizaciones(tipo, nombres, dato):
    if tipo == "perdida":
        if dato[0]> 0:
            #print("No hay cotizaciones con pérdida")
            devolver = []
            return devolver
        elif dato[1]>0:
            #print("La cotización con mayor pérdida es: \n" + str(nombres[0]) , "con una valor de " + str(dato[0]))
            devolver = [{nombres[0]:dato[0]}]
            return devolver
        else:
            #print("Las cotizaciones con mayor pérdida son: \n" + str(nombres[0]) , " con una valor de: ", str(dato[0]), "\n " , str(nombres[1]) , " con una valor de: ", str(dato[1]))
            devolver = [{nombres[0]:dato[0]}, {nombres[1]:dato[1]}]
            return devolver
    if tipo == "ganancia":
        if dato[-1]< 0:
            devolver = []
            return devolver
        elif dato[-2] <0:
            #print("La cotización con mayor ganancia es \n" + str(nombres[-1]) , "con una valor de " + str(dato[-1]))
            devolver = [{nombres[-1]:dato[-1]}]
            return devolver
        else:
            #print("Las cotizaciones con mayor pérdida son: \n" + str(nombres[-2]) , " con una valor de: ", str(dato[-2]), "\n " , str(nombres[-1]) , " con una valor de: ", str(dato[-1]) )
            devolver =[{nombres[-1]:dato[-1]}, {nombres[-2]:dato[-2]}]
            return devolver

