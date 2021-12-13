import csv

def costo_camion(nombre_archivo):
    '''
    Calcula el costo total de la mercadería de un camión.
    '''

    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        costo_total = 0
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return costo_total
