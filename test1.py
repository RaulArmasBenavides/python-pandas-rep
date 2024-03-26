import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
lista = [25,50,75,100]


obj=pd.Series(data=lista)
print(obj)

ahorros = np.random.randint(100,size=[6])
meses =['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

plt.plot(ahorros)
plt.show()



plt.plot(np.random.randint(100,size=[6]))
plt.plot(np.random.randint(100,size=[6]))
plt.plot(np.random.randint(100,size=[6]))


plt.xticks(mapeado,meses)
plt.xlim(1,4)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad")
plt.legend(["Pedro","Ana","Raul"])
plt.show()
