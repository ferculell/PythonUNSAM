import random
import numpy as np

def crear_album(figus_total):
    '''
    Crea un vector de ceros con la cantidad de espacios pasado por parámetro.
    '''
    return np.zeros(figus_total)

def album_incompleto(A):
    return (np.count_nonzero(A) < len(A))

def comprar_figu(figus_total):
    return random.randint(1, figus_total)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    cantidad_comprada = 0
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu-1] += 1
        cantidad_comprada += 1
    return cantidad_comprada

def experimento_figus(n_repeticiones, figus_total):
    resultados = []
    for i in range(n_repeticiones):
        resultados.append(cuantas_figus(figus_total))
    return np.mean(resultados)
