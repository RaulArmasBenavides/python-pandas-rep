import pandas as pd
import random

# Lista para almacenar las transacciones
lista = [] 

# Clase Transaccion
class Transaccion:
    def __init__(self, num_cajero, DNI, tipo, monto):
        self.num_cajero = num_cajero
        self.DNI = DNI
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        return f"El titular de la cuenta con DNI: {self.DNI} ha realizado la transacción {self.tipo} con monto S/.{self.monto}"

    def __del__(self):
        print("Destruyendo objeto")

# Funciones
def registrar_transaccion(num_cajero, dni):
     tipo = input("Ingresar el tipo de la transacción: ")
     monto = float(input("Ingresar monto S/.: "))
     return Transaccion(num_cajero, dni, tipo, monto)

def encontrar_mayor_monto_transaccion():
    if lista:
        transaccion_mayor_monto = max(lista, key=lambda x: x.monto)
        print(f"La transacción con mayor monto es {transaccion_mayor_monto.tipo} de S/.{transaccion_mayor_monto.monto}")

def agrupar_transacciones():
     if lista:
         df = pd.DataFrame([vars(o) for o in lista])
         df['monto'] = pd.to_numeric(df['monto'], errors='coerce')
         print("Listando las transacciones agrupadas por tipo de transacción")
         print(df.groupby(['tipo']).agg({'monto': ['mean', 'count']}))
         print("Contando las transacciones por cajero")
         print(df.groupby(['num_cajero']).agg({'monto': ['count']}))

# Bloque principal
print("########## REGISTRO DE TRANSFERENCIA ###########")
cajeros = "1234567"

while True:
    dni = input("Ingrese DNI (o escriba 'ok' para finalizar): ")
    if dni.lower() == "ok":
        break
    num_cajero = random.choice(cajeros)
    lista.append(registrar_transaccion(num_cajero, dni))

for obj in lista:
    print(obj)

encontrar_mayor_monto_transaccion()
agrupar_transacciones()