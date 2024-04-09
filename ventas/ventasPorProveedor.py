from __future__ import print_function, division
from builtins import range
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    tabla = pd.read_csv('ventas\VentasPorProveedor.csv', skiprows=5)
    print(tabla.info())
    print(tabla.index[22])