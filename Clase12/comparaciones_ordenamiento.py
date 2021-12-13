import random
import matplotlib.pyplot as plt


def generar_lista(N):
    return [random.randint(1, 1000) for i in range(N)]


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    counter = 0

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        #p = buscar_max(lista, 0, n)
        counter += buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        #lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return counter

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    #pos_max = a
    count = 0
    for i in range(a + 1, b + 1):
        count += 1
        #if lista[i] > lista[pos_max]:
            #pos_max = i
    return count


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    counter = 0

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        counter += 1
        if lista[i + 1] < lista[i]:
            #reubicar(lista, i + 1)
            counter += reubicar(lista, i + 1)
        #print("DEBUG: ", lista)

    #return lista
    return counter

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    count = 0
    while j > 0 and v < lista[j - 1]:
        count += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return count


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
    counter = 0
    while n > 0:
        for i in range(n):
            counter += 1
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
        #print("DEBUG: ", i, n, lista)
        n -= 1
    #return lista
    return counter


def merge_sort(lista, counter):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, counter_iz = merge_sort(lista[:medio], counter)
        der, counter_der = merge_sort(lista[medio:], counter)
        lista_nueva, count = merge(izq, der)
        counter += (counter_iz + counter_der + count)
    return lista_nueva, counter

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    count = 0

    while(i < len(lista1) and j < len(lista2)):
        count += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, count


def experimento(N, k):
    sum_seleccion = 0
    sum_insercion = 0
    sum_burbujeo = 0
    sum_merge = 0
    for i in range(k):
        lista = generar_lista(N)
        sum_seleccion += ord_seleccion(lista.copy())
        sum_insercion += ord_insercion(lista.copy())
        sum_burbujeo += ord_burbujeo(lista.copy())
        sum_merge += merge_sort(lista.copy(), 0)[1]
    
    return sum_seleccion / k, sum_insercion / k, sum_burbujeo / k, sum_merge / k


def experimento_vectores(Nmax):
    comparaciones_seleccion = []
    comparaciones_insercion = []
    comparaciones_burbujeo = []
    comparaciones_merge = []
    largos = range(1, Nmax)
    for N in largos:
        lista = generar_lista(N)
        comparaciones_seleccion.append(ord_seleccion(lista.copy()))
        comparaciones_insercion.append(ord_insercion(lista.copy()))
        comparaciones_burbujeo.append(ord_burbujeo(lista.copy()))
        comparaciones_merge.append(merge_sort(lista.copy(), 0)[1])
    
    plt.plot(largos, comparaciones_seleccion, label='Selección')
    plt.plot(largos, comparaciones_insercion, label='Inserción')
    plt.plot(largos, comparaciones_burbujeo, label='Burbujeo', linestyle='dotted', color='red')
    plt.plot(largos, comparaciones_merge, label='Merge')
    plt.ylim(0, 30000)
    plt.xlim(0, 300)
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.text(10, 15000, 'La complejidad no crece de manera\nexponencial con el método Merge Sort\ncomo sucede con los otros métodos.')
    plt.show()
