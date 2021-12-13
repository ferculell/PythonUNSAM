import informe_final

def costo_camion(nombre_archivo):
    '''
    Calcula el costo total de la mercadería de un camión.
    '''

    camion = informe_final.leer_camion(nombre_archivo)
    return camion.precio_total()


def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion')
    print(f'Costo total: {costo_camion(parametros[1])}')


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)