import random
import matplotlib.pyplot as plt
import timeit as tt
import numpy as np



def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1

    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)

    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v


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
        n -= 1
    return lista


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


def generar_lista(N):
    return [random.randint(1, 1000) for i in range(N)]

def generar_listas(Nmax):
    listas = []
    for N in range(1, Nmax):
        listas.append(generar_lista(N))
    return listas

def experimento_timeit(Nmax):
    listas = generar_listas(Nmax)
    num = 50   # número de iteraciones para el método timeit
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge = []

    global lista

    for lista in listas:

        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = num, globals = globals())

        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_merge.append(tiempo_merge)

    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_merge = np.array(tiempos_merge)

    return tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_merge


def graficar_experimento(Nmax):
    seleccion, insercion, burbujeo, merge = experimento_timeit(Nmax)

    plt.plot(seleccion, label='Selección')
    plt.plot(insercion, label='Inserción')
    plt.plot(burbujeo, label='Burbujeo')
    plt.plot(merge, label='Merge')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Tiempo de ejecución")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()