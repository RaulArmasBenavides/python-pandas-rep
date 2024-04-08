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