def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos


def donde_insertar(lista, x, verbose=False):
    '''
    Precondición: la lista está ordenada
    Devuelve la posición donde debería ubicarse el elemento buscado.
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = 0 # Inicializo respuesta en cero
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        pos = medio     # guardo la posición del medio
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] >= x and lista[medio - 1] < x:
            break     # posición encontrada, corto el ciclo
        elif lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos


def insertar(lista, x):
    '''
    Precondición: la lista está ordenada
    Devuelve la posición donde debería ubicarse el elemento buscado
    y lo inserta en la lista si es que no está en ella.
    '''
    pos = 0 # Inicializo respuesta en cero
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        pos = medio     # guardo la posición del medio
        if lista[medio] == x:
            break     # elemento encontrado!
        elif lista[medio] > x and lista[medio - 1] < x:
            lista.insert(medio, x) # posición encontrada, inserto el elemento
            break     # corto el ciclo
        elif lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos