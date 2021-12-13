import csv

def leer_camion(nombre_archivo):
    '''
    Devuelve el contenido de mercadería de un camión en forma de tupla.
    '''

    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        for n_row, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                lote = {
                        'nombre': record['nombre'], 
                        'cajones': int(record['cajones']), 
                        'precio': float(record['precio'])
                       }
                camion.append(lote)
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
        return camion


def leer_precios(nombre_archivo):
    '''
    Devuelve una lista de precios.
    '''

    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        lista_precios = {}
        for row in rows:
            try:
                lista_precios[row[0]] = float(row[1])
            except:
                print('Warning: there are missing values.')
        return lista_precios


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
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return costo_total


def informe(archivo_camion, archivo_precios):
    '''
    Devuelve un iforme con el balance de la venta de meradería por camión.
    '''

    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    valor_compra = 0.0
    valor_venta = 0.0

    for fila in camion:
        valor_compra += fila['cajones'] * fila['precio']
        valor_venta += fila['cajones'] * precios[fila['nombre']]
    balance = valor_venta - valor_compra

    print(f'El costo de la mercadería es de ${valor_compra}')
    print(f'El monto recaudado con la venta es ${valor_venta}')
    if balance > 0:
        print(f'La ganancia es de ${balance}')
    else:
        print(f'La pérdida es de ${abs(balance)}')
