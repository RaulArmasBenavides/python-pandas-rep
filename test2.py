import pandas as pd
if __name__ == "__main__":
    df = pd.DataFrame({
        'enteros':[100,200,300,400],
        'decimales':[3.14,2.52,1.533,6.6],
        'cadenas':['hola','tio','diego','odegard']
    })
    print(df)
    res = df['cadenas'].apply(len)
    print(res)

    datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}
    contabilidad = pd.DataFrame(datos)
    print(contabilidad)

    #ventas de bazar yuliza
    df = pd.DataFrame({
    'tienda': ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C'],
    'producto': ['X', 'X', 'Y', 'Z', 'Y', 'Z', 'X', 'Y'],
    'unidades_vendidas': [110, 90, 150, 200, 130, 80, 60, 175]
    })
    # filtra aquellos registros que corresponden a ventas mayores a 100 unidades y calcula el total de ingresos (asumiendo que cada unidad se vende a $5.00). 
    ##Luego, agrega una nueva columna al DataFrame filtrado que muestre los ingresos por venta.

    # Ejercicio 1
    indices_filtrados = df['unidades_vendidas'] > 100
    df.loc[indices_filtrados, 'ingresos'] = df.loc[indices_filtrados, 'unidades_vendidas'] * 5

    print(df)
    df_agrupado = df.groupby('tienda').agg(
        total_unidades=pd.NamedAgg(column='unidades_vendidas', aggfunc='sum'),
        promedio_unidades=pd.NamedAgg(column='unidades_vendidas', aggfunc='mean')
    )
    print(df_agrupado)