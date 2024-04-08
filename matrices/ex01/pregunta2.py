import numpy as np

# Validaciones de los datos de ingreso
def validar_entero(n):
    while True:
        try:
            return int(n)
        except ValueError:
            n = input("Caracter no valido, ingrese un entero: ")

def validar_decimal(n):
    while True:
        try:
            return float(n)
        except ValueError:
            n = input("Caracter no valido, ingrese un decimal: ")

def ns(c):
    while c not in ["s", "n"]:
        c = input("Escribe solo 'n' o 's' según su opción: ")
    return c

# Función para definir matriz
def crea_matriz(fil, col):
    matriz = []
    for f in range(1, fil+1):
        fila = []
        for c in range(1, col+1):
            valor = validar_decimal(input(f'Registrar el elemento ({f},{c}): '))
            fila.append(valor)
        matriz.append(fila)
    return np.array(matriz, dtype=float)

# Main loop
if __name__ == "__main__":
    while True:
        print("          CALCULADORA DE MATRICES          ") 
        # Omitimos la tabla de operadores para simplificar
        
        fil = validar_entero(input("Indique número de filas: "))
        col = validar_entero(input("Indique número de columnas: "))
        
        A = crea_matriz(fil, col)
        B = crea_matriz(fil, col)
        
        print("\nMatriz A:\n", A)
        print("\nMatriz B:\n", B)
        
        while True:
            oper = input("Introduzca operador: ")
            while oper not in ["+", "-", "*", "C"]:
                oper = input("Introduzca un operador válido: ")
            
            if oper == "+":
                resultado = A + B
            elif oper == "-":
                resultado = A - B
            elif oper == "*":
                resultado = np.dot(A, B)
            else:
                break
            
            print("\nRESULTADO\n", resultado)

        conti = ns(input("¿Reiniciar cálculos? (n para finalizar): "))
        if conti == "n":
            break