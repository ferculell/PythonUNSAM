import csv

def leer_camion(nombre_archivo):
    '''
    Devuelve el contenido de mercadería de un camión y el encabezado 
    de los datos, todo en forma de tupla.
    '''

    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        for row in rows:
            try:
                lote = {'nombre': row[0], 'cajones': int(row[1]), 'precio': float(row[2])}
                camion.append(lote)
            except ValueError:
                print('Warning: there are missing values.')
        return camion, headers


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
                print('Warning: there are missing values.\n\n')
        return lista_precios


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
        

def hacer_informe(camion, precios):
    '''
    Devuelve una lista de tuplas.
    '''
    
    lista = []
    for fila in camion:
        tupla = (fila['nombre'], fila['cajones'], fila['precio'], (precios[fila['nombre']] - fila['precio']))
        lista.append(tupla)
        
    return lista

# Carga y procesa los datos
camion, headers = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe_hecho = hacer_informe(camion, precios)

#Imprime el resultado
print(f'{headers[0].capitalize():>10s} {headers[1].capitalize():>10s} {headers[2].capitalize():>10s} {"Cambio":>10s}')
print('---------- ' * 4)
for nombre, cajones, precio, cambio in informe_hecho:
    precio_formateado = "${:,.2f}".format(precio)
    print(f'{nombre:>10s} {cajones:>10d} {precio_formateado:>10s} {cambio:>10.2f}')
