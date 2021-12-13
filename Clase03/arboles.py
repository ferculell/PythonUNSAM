import csv
from collections import Counter


def leer_parque(nombre_archivo, parque):
    '''
    Devuelve una lista de diccionarios con la info de cada árbol de determinado parque
    '''

    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        arboles = []
        for n_row, row in enumerate(rows, start=1):
            if row[10] == parque:
                arbol = dict(zip(headers, row))
                arboles.append(arbol)
            
#            try:
#                lote = {
#                        'nombre': record['nombre'], 
#                        'cajones': int(record['cajones']), 
#                        'precio': float(record['precio'])
#                       }
#                camion.append(lote)
#            except ValueError:
#                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return arboles


def especies(lista_arboles):
    lista_especies = []
    for item in lista_arboles:
        lista_especies.append(item['nombre_com'])
    return set(lista_especies)


def contar_ejemplares(lista_arboles):
    existencias = Counter()
    for item in lista_arboles:
        existencias[item['nombre_com']] += 1
    return existencias