
import numpy as np
list=[i for i in range(100)]
pares=[]
impares=[]
def paridad(x):
    if x%2==0:
        return True
    else:
        return False

for numero in list:
    if paridad(numero):
        pares.append(numero)
    else:
        impares.append(numero)
pares=  np.array(pares)
impares= np.array(impares)
print(pares)
print(impares)
