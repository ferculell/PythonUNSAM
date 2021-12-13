import csv

def costo_camion(nombre_archivo):
    '''
    Calcula el costo total de la mercadería de un camión.
    '''

    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        suma = 0
        for row in rows:
            try:
                valor_cajon = int(row[1]) * float(row[2])
                suma += valor_cajon
            except ValueError:
                print('Warning: there are missing values.')
        return suma
