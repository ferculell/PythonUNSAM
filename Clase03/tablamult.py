digitos = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
matriz_tablas = []

for digito in digitos:
    tabla = 0
    lista_tabla = []
    for i in range(10):
        tabla += digitos[digito - 1]
        lista_tabla.append(tabla)
    matriz_tablas.append(lista_tabla)
    
print('   {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d}'.format(*digitos))
print('-' * 63)
for i, row in enumerate(matriz_tablas):
    print(f'{i+1:2d}:' + ''.join('{:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d}'.format(*row)))

