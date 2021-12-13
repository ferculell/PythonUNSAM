import datetime

def vida_en_segundos(fecha_nac):
    '''
    Calcula los segundos vividos por una persona hasta ahora, dada su fecha de nacimiento.
    Recibe como entrada una cadena en formato "dd/mm/AAAA".
    Devuelve un float.
    '''
    nacimiento = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
    ahora = datetime.datetime.now()
    resultado = ahora - nacimiento
    return resultado.total_seconds()