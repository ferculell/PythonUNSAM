def diccionario_geringoso(lista):
    '''
    Construye un diccionario de geringoso
    simple a partir de una lista de palabras
    '''

    diccionario = {}
    for palabra in lista:
        capadepenapa = ''
        for c in palabra:
            if c == 'a':
                capadepenapa = capadepenapa + c + 'pa'
            elif c == 'e':
                capadepenapa = capadepenapa + c + 'pe'
            elif c == 'i':
                capadepenapa = capadepenapa + c + 'pi'
            elif c == 'o':
                capadepenapa = capadepenapa + c + 'po'
            elif c == 'u':
                capadepenapa = capadepenapa + c + 'pu'
            else:
                capadepenapa = capadepenapa + c
        diccionario[palabra] = capadepenapa

    return diccionario
