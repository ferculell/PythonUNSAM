#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: Habían dos errores semánticos en el código
#El primero lo solucioné agregando el método lower() a la letra de entrada
# antes de comparar.
#El segundo lo corregí sacando el return False de la estructura condicional
# colocándolo antes de finalizar el bloque del ciclo while.
#Elcódigo corregido es el siguiente
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        else:
            i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.2. Función tiene_a()
#Comentario: Habían varios errores de sintaxis en el código original.
# Faltaban los dos puntos en las sentencias de definición
# de la función, del ciclo while y del condicional.
# En el condicional se estaba utilizando un signo de asignación en lugar
# del operador lógico de comparación.
# También había un error en el nombre del valor booleano False.
# El error semántico que no permitía reconocer mayúsculas fue corregido
# incorporando el método lower() al caracter a comparar.
#El código corregido es el siguiente.
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El código no puede procesar entradas de tipo numérico.
# Realicé una conversión a tipo string de la entrada para solucionarlo.
#El código corregido es el siguiente
def tiene_uno(expresion):
    str_expresion = str(expresion)
    n = len(str_expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if str_expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)


#%%
#Ejercicio 3.4. Función suma()
#Comentario: El problema es que en el modo en que la función está definida,
# no está retornando ningún valor. Lo solucioné reemplazando la asignación
# a la variable c por un return.
#El código corregido es el siguiente
def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#%%
#Ejercicio 3.5. Función leer_camion()
#Comentario: Al encontrarse la variable registro en un scope global
# con respecto al ciclo for, se estaba sobrescribiendo el mismo diccionario
# para todas las filas. Lo solucioné llevando esa variable hacia el interior
# del ciclo for.
#El código corregido es el siguiente
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
