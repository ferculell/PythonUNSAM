def pascal(n, k):
    '''
    Calcula el valor que se encuentra en la fila n y la columna k
    para un Triángulo de Pascal.
    Acepta como parámetros números positivos enteros.
    k debe ser menor o igual a n.
    '''
    if k == 1 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)