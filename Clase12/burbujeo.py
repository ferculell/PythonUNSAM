def ord_burbujeo(lista):
    '''
    Implementa el algoritmo de ordenamiento por burbujeo.
    Este algoritmo tiene una complejidad de O(N^2) porque debe realizar
    una cantidad de aproximadamente N * N/2 comparaciones, al recorrer
    N veces la lista dejando fuera un elemento en cada vuelta.
    Recibe una lista con elementos comparables.
    Devuelve la misma lista ordenada.
    '''
    n = len(lista) - 1
    while n > 0:
        for i in range(n):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
        #print("DEBUG: ", i, n, lista)
        n -= 1
    return lista