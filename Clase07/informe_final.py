#!/usr/bin/env python3
# informe_final.py

import fileparse

def leer_camion(nombre_archivo):
    '''
    Devuelve el contenido de mercadería de un camión en una lista de diccionarios.
    '''

    with open(nombre_archivo) as lines:
        camion = fileparse.parse_csv(lines, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        return camion


def leer_precios(nombre_archivo):
    '''
    Devuelve una lista de precios en forma de diccionario.
    '''

    with open(nombre_archivo) as lines:
        return dict(fileparse.parse_csv(lines, types = [str, float], has_headers=False))


def informe(archivo_camion, archivo_precios):
    '''
    Devuelve un informe con el balance de la venta de meradería por camión.
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


def imprimir(headers, informe_hecho):
    '''
    Imprime el informe.
    '''
    print(f'{headers[0].capitalize():>10s} {headers[1].capitalize():>10s} {headers[2].capitalize():>10s} {"Cambio":>10s}')
    print('---------- ' * 4)
    for nombre, cajones, precio, cambio in informe_hecho:
        precio_formateado = "${:,.2f}".format(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio_formateado:>10s} {cambio:>10.2f}')


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    '''
    Recibe dos rutas en formato string a archivos csv.
    Devuelve una lista con los headers y el informe hecho.
    '''
    camion = leer_camion(nombre_archivo_camion)
    headers = list(camion[0].keys())
    precios = leer_precios(nombre_archivo_precios)
    informe_hecho = hacer_informe(camion, precios)
    imprimir(headers, informe_hecho)
    informe(nombre_archivo_camion, nombre_archivo_precios)


def f_principal(parametros):
    if len(parametros) != 3:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    return informe_camion(parametros[1], parametros[2])


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)


#informe_camion('../Data/camion.csv', '../Data/precios.csv')