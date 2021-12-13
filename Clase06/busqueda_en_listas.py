def busqueda_lineal_lordenada(lista,e):
    '''
    Busca un elemento en una lista ordenada y devuelve su posición.
    Si no lo encuentra devuelve -1.
    '''
    
    for i, item in enumerate(lista):
        if item == e:
            return i
        elif item > e:
            return -1
    
    return -1

