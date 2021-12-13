
from vigilante import vigilar
import csv


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0, 1, 2]] for row in rows)
    rows = ([func(val) for func, val in zip([str, float, int], row)] for row in rows)
    rows = (dict(zip(['nombre', 'precio', 'volumen'], row)) for row in rows)
    return rows


def ticker(camion_file, log_file, fmt):
    from formato_tabla import crear_formateador
    import informe_final
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = (fila for fila in rows if fila['nombre'] in camion)
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        rowdata = [row['nombre'], str(row['precio']), str(row['volumen'])]
        formateador.fila(rowdata)


if __name__ == '__main__':

    # lines = vigilar('../Data/mercadolog.csv')
    # rows = parsear_datos(lines)
    # for row in rows:
    #     print(row)

    import informe_final
    camion = informe_final.leer_camion('../Data/camion.csv')
    rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
    rows = (fila for fila in rows if fila['nombre'] in camion)
    for row in rows:
        print(row)