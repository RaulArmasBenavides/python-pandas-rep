import pandas as pd
# creamos la clase Servico
class Servicio:
    unidad = ""
    monto  =0
 

def registrarServicio():
    s = Servicio()
    s.unidad = input("Ingresar unidad del servicio: ")
    while True:
        try:
            s.monto = float(input("Ingresar monto: "))
            break  
        except ValueError:
            print("Por favor, ingrese un número válido para el monto.")
    return s

def listarServicio(lista):
    for s in lista:
     print (s.unidad ," Monto ", s.monto)

def search(valor , lista):
    for x in lista:
        if x.monto == valor:
          print("El servicio con mayor monto es ",x.unidad,x.monto)
          break
    else:
        x = None
   
def EncontrarMayorMontoServicio(lista):
    hiscore = 0
    for x in lista:
       count = 0
       if x.monto > hiscore:
              hiscore = x.monto
              count += 1
    print("El mayor monto es  ",hiscore)
    search(hiscore,lista)


def listarServicioAgrupados(lista):
     df = pd.DataFrame(o.__dict__ for o in lista)
     print("Listando los servicios")
     print(df)
     df.groupby(['unidad'])['monto'].sum().reset_index()
     print("Listando los servicios acumulados")
     print( df.groupby(['unidad'])['monto'].sum().reset_index())


if __name__ == "__main__":
    # bloque principal
    lista = list()
    name = input("########## REGISTRO SEMANAL DE REGISTROS POR UNIDAD  ###########")
    while name != "ok":
        name = input("########### Ingresar los datos. Escriba ok para finalizar el programa  ###########")
        if name !="ok":
         s = registrarServicio()
         lista.append(s);
    
    listarServicio(lista)
    EncontrarMayorMontoServicio(lista)
    listarServicioAgrupados(lista)
