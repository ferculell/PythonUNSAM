#!/usr/bin/env python3
# informe_final.py

import fileparse
import lote
import formato_tabla

def leer_camion(nombre_archivo):
    '''
    Devuelve el contenido de mercadería de un camión en una lista de diccionarios.
    '''

    with open(nombre_archivo) as lines:
        camion_dicts = fileparse.parse_csv(lines, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
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
        valor_compra += fila.cajones * fila.precio
        valor_venta += fila.cajones * precios[fila.nombre]
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
        tupla = (fila.nombre, fila.cajones, fila.precio, (precios[fila.nombre] - fila.precio))
        lista.append(tupla)
        
    return lista


def imprimir_informe(informe_hecho, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe_hecho:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt="txt"):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)

    # Crear los datos para el informe
    informe_hecho = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe_hecho, formateador)
    #informe(nombre_archivo_camion, nombre_archivo_precios)


def f_principal(parametros):
    if len(parametros) != 3 and len(parametros) != 4:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios [formato]')
    elif len(parametros) == 3:
        return informe_camion(parametros[1], parametros[2])
    elif len(parametros) == 4:
        return informe_camion(parametros[1], parametros[2], parametros[3])


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)


#informe_camion('../Data/camion.csv', '../Data/precios.csv')