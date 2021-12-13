import random
from collections import Counter


def tirar():
    '''
    Devuelve los resultados aleatorios de una tirada de 5 dados.
    '''
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1, 6))
    return tirada


def tirar_de_nuevo(seleccion):
    '''
    Recibe una lista con los resultados coincidentes de una tirada anterior
    y la completa con resultados aleatorios hasta llegar a 5 dados.
    '''
    tirada = seleccion
    while len(tirada) < 5:
        tirada.append(random.randint(1, 6))
    return tirada


def seleccionar(tirada):
    '''
    Recibe una lista con una tirada de dados y devuelve una lista con la selección
    de los valores repetidos.
    '''
    contador = Counter(tirada)
    dado, cantidad = contador.most_common(1)[0]
    return ([int(dado) * cantidad])


def es_generala(tirada):
    '''
    Recibe una lista de resultados y devuelve True corresponde a generala.
    '''
    for dado in tirada:
        if dado != tirada[0]:
            return False
    return True


def tres_tiradas():
    '''
    Realiza tres tiradas guardando los resultados coincidentes
    '''
    tirada = tirar()
    for i in range(2):
        seleccion = seleccionar(tirada)
        tirada = tirar_de_nuevo(seleccion)
    return tirada


def prob_generala(N):
    '''
    Estima la probabilidad de obtener una generala al finalizar una mano de tres tiradas
    utilizando una simulación con N iteraciones.
    '''
    G = sum([es_generala(tres_tiradas()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} manos de tres tiradas, de las cuales {G} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    

def test(N):
    '''
    Estima la probabilidad de obtener una generala al finalizar una mano de tres tiradas
    utilizando una simulación con N iteraciones.
    '''
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    