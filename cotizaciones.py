import matplotlib

#Identificar las 2 cotizaciones de mayor ganancia y de mayor perdida.


#df = df.sort_values([info_header], ascending=True)     Codigo para tener la tabla antes hecha ordenada





def cotizaciones():
    ganancias_perdidas = [{}]

    largo_df = len(df)

    mayor_perdida = df[0]       

    for i in range(len(df)):
        if df[i]== mayor_perdida:
            df[i]["Name"] = nombre_mayor_perdida
            ganancias_perdidas["nombre_ganancia"]= nombre_mayor_perdida
            ganancias_perdidas["valor_ganancia"]= df[0]

        if df[largo_df]== mayor_ganancia:
            df[i]["Name"] = nombre_mayor_ganancia
            ganancias_perdidas["nombre_ganancia"]= nombre_mayor_ganancia
            ganancias_perdidas["valor_ganancia"]= df[largo_df]    
        
    
    names = ganancias_perdidas["nombre_ganancia"]
    porcentajes = ganancias_perdidas["valor_ganancia"]

    matplotlib.rcParams["figure.figsize"] =10 , 5
        pyplot.scatter(porcentajes, names, edgecolors="black", linewidths=1,alpha=0.75)
        pyplot.title("  MAYORES PERDIDAS Y GANANCIAS")
        pyplot.xlabel("PORCENTAJE")
        pyplot.ylabel("EMPRESAS")

        pyplot.tight_layout()
        pyplot.show()


if __name__ == '__main__':
    print("Cotizaciones") 