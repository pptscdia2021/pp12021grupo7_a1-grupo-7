if __name__ == '__main__':
    print("Cotizaciones") 

#Identificar las 2 cotizaciones de mayor ganancia y de mayor perdida.

#si los cotizaciones están en una lista:

nombres=[]
max_ganancia=[]
min_ganancia=[]

mayor_maximo = max(max_ganancia)
menor_minimo = min(min_ganancia)

for i in range(len(max_ganancia)):
    if mayor_maximo == max_ganancia[i]:
        nombre_max = i
    else:
        pass

for i in range(len(min_ganancia)):
    if menor_minimo == min_ganancia[i]:
        nombre_min = i
    else:
        pass
print(nombres[nombre_max])
print(nombres[nombre_min])




#en caso que debamos usar oop
class bolsa_valores:
    def __init__(self, nombre , max_ganancia , min_ganancia):
        self.nombre = nombre
        self.max_ganancia = max_ganancia
        self.min_ganancia = min_ganancia

