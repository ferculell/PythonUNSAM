def propagar(lista):
    '''
    Recibe un vector con 0's, 1's y -1's 
    y devuelve un vector en el que los 1's se propagaron a sus vecinos con 0.
    '''
    
    #Indicador de propagación
    propagacion = False
    
    #Invierte la lista para la primera pasada
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    
    for i, e in enumerate(invertida):
        if e == 1:
            propagacion = True
        elif e == -1:
            propagacion = False
        elif e == 0 and propagacion == True:
            invertida[i] = 1
    
    #Invierte nuevamente la lista para la segunda pasada
    restituida = []
    for e in invertida:
        restituida.insert(0, e)
    
    for i, e in enumerate(restituida):
        if e == 1:
            propagacion = True
        elif e == -1:
            propagacion = False
        elif e == 0 and propagacion == True:
            restituida[i] = 1
    
    return restituida
    
