import csv

def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    filas = csv.reader(lines)

    if select and has_headers == False:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    
    if has_headers:

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for i, fila in enumerate(filas):
            try:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                # Parsear los valores si se especifica el tipo
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]

                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            except ValueError as e:
                if not silence_errors:
                    print(f'Fila {i+1}: No pude convertir {fila}')
                    print(f'Fila {i+1}: Motivo: {e}')

        return registros
    
    else:

        registros = []
        for i, fila in enumerate(filas):
            try:
                if not fila:    # Saltear filas vacías
                    continue
                # Parsear los valores si se especifica el tipo
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]

                # Armar la tupla
                registro = tuple(fila)
                registros.append(registro)
            except ValueError as e:
                if not silence_errors:
                    print(f'Fila {i+1}: No pude convertir {fila}')
                    print(f'Fila {i+1}: Motivo: {e}')

        return registros

    

