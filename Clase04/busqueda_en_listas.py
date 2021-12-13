def buscar_u_elemento(lista, elemento):
    '''
    Busca un elemento en una lista y devuelve su posición.
    Si no lo encuentra devuelve -1.
    '''
    
    indice = -1
    
    for i, item in enumerate(lista):
        if item == elemento:
            indice = i
    
    return indice


def buscar_n_elemento(lista, elemento):
    '''
    Busca un elemento en una lista y devuelve la cantidad de veces que aparece.
    '''
    
    cantidad = 0
    
    for item in lista:
        if item == elemento:
            cantidad += 1
    
    return cantidad


def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía. Funciona con números positivos o negativos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo con el primer elemento de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m


def minimo(lista):
    '''Devuelve el mínimo de una lista, 
    la lista debe ser no vacía. Funciona con números positivos o negativos.
    '''
    # m guarda el mínimo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo con el primer elemento de la lista
    for e in lista: # Recorro la lista y voy guardando el menor
        if e < m:
            m = e
    return m


