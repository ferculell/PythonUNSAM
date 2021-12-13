import csv

def leer_arboles(nombre_archivo, encoding="utf-8"):
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


def ver_alturas(arboleda, tipo_arbol):
    '''
    Devuelve una lista con las alturas del tipo de árbol seleccionado.
    El primer parámetro debe ser una lista de diccionarios y el segundo un string.
    '''
    
    alturas = [float(arbol['altura_tot'])
               for arbol in arboleda 
               if arbol['nombre_com'] == tipo_arbol]
    return alturas
    

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
    

def medidas_de_especies(especies, arboleda):
    '''
    Devuelve un diccionario con la lista de tuplas de alturas y diámetros para cada entrada.
    El primer parámetro debe ser una lista de strings y el segundo una lista de diccionarios.
    '''
    
    resultado = {nombre: ver_alturas_diametros(arboleda, nombre) for nombre in especies}
    return resultado

   