"""
Simulacion distribución de temperaturas en una ciudad a lo largo de un mes
"""
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    # Paso 1: Generar datos simulados
    np.random.seed(0)  # Para reproducibilidad
    dias_del_mes = 30
    temperaturas = np.random.normal(loc=22, scale=5, size=dias_del_mes)  # Temperatura promedio 22, desviación 5
    temperaturas = np.sort(temperaturas)  # Simula una tendencia de cambio en las temperaturas

    # Paso 2: Visualizar los datos
    plt.figure(figsize=(10, 6))
    plt.plot(temperaturas, marker='o', linestyle='-', color='b')
    plt.title('Temperaturas Máximas Diarias en un Mes')
    plt.xlabel('Día del Mes')
    plt.ylabel('Temperatura Máxima (°C)')
    plt.grid(True)
    plt.show()