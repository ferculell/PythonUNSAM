import informe_funciones

def costo_camion(nombre_archivo):
    '''
    Calcula el costo total de la mercadería de un camión.
    '''

    costo_total = 0
    camion = informe_funciones.leer_camion(nombre_archivo)
    for fila in camion:
        costo_total += fila['cajones'] * fila['precio']
    return costo_total
