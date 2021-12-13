import os
import sys


def archivos_png(directorio):
    '''
    Arma una lista de todos los archivos .png que se encuentren 
    en algún subdirectorio del directorio dado.
    Recibe la ruta de un directorio en formato string.
    Devuelve una lista de strings.
    '''
    result = []
    for _, dirs, files in os.walk(directorio):
        for name in files:
            if name.split('.')[-1] == 'png':
                result.append(name)
        for name in dirs:
            if name.split('.')[-1] == 'png':
                result.append(name)
    print(result)       


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio_seleccionado')
    archivos_png(sys.argv[1])