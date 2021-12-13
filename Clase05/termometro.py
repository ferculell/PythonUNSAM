import random
import numpy as np

def medir_temp(n):
    mediciones = []
    for i in range(n):
        mediciones.append(37.5 + random.normalvariate(0, 0.2))
    temperaturas = np.array(mediciones)
    np.save('../Data/temperaturas', temperaturas)
    return mediciones

def resumen_temp(n):
    mediciones = medir_temp(n)
    maxima = max(mediciones)
    minima = min(mediciones)
    promedio = sum(mediciones) / n
    mediana = 0
    if n % 2 == 0:
        mediana = (mediciones[n//2-1] + mediciones[n//2]) / 2
    else:
        mediana = mediciones[n//2]
    return (maxima, minima, promedio, mediana)
