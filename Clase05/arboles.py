import csv
import matplotlib.pyplot as plt
import numpy as np

def leer_parque(nombre_archivo):
    '''
    Devuelve una lista de diccionarios con la info de cada árbol
    '''

    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        arboleda = []
        for n_row, row in enumerate(rows, start=1):
            arbol = dict(zip(headers, row))
            arboleda.append(arbol)
        return arboleda

def ver_alturas_diametros(arboleda, tipo_arbol):
    '''
    Devuelve una lista de tuplas con las alturas y diámetros del tipo de árbol seleccionado.
    El primer parámetro debe ser una lista de diccionarios y el segundo un string.
    '''
    
    alturas = [float(arbol['altura_tot'])
               for arbol in arboleda 
               if arbol['nombre_com'] == tipo_arbol]
    diametros = [float(arbol['diametro'])
               for arbol in arboleda 
               if arbol['nombre_com'] == tipo_arbol]
    resultado = list(zip(alturas, diametros))
    return resultado

def histograma_altura():
    arboleda = leer_parque('../Data/arbolado-en-espacios-verdes.csv')
    alturas = [float(arbol['altura_tot'])
               for arbol in arboleda 
               if arbol['nombre_com'] == 'Jacarandá']
    plt.hist(alturas, bins=50)
    plt.show()

def scatter_hd(lista_de_pares):
    array_de_pares = np.array(lista_de_pares)
    d = array_de_pares[:,0]
    h = array_de_pares[:,1]
    plt.scatter(d,h)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()

