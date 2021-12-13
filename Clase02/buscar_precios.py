def buscar_precio(fruta):
    '''
    Busca el precio de una fruta y lo imprime.
    '''

    with open('../Data/precios.csv') as precios:
        encontrado = False
        for line in precios:
            row = line.split(',')
            if row[0] == fruta:
                print('El precio de un cajón de', fruta, 'es:', row[1])
                encontrado = True
        if not encontrado:
            print(fruta, 'no figura en el listado de precios.')
