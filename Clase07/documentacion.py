def valor_absoluto(n):
    '''
    Devuelve el valor absoluto de un número dado.
    Pre: Acepta números positivos o negativos.
    Pos: Devuelve un número positivo correspondiente al valor absoluto.
    '''
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    '''
    Devuelve la suma de los números pares presentes en una lista.
    Pre: Acepta un iterable.
    Pos: Devuelve la suma de los números pares.
         Si el iterable es vacío, devuelve 0.
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
    # el invariante de ciclo de esta función es la variable res


def veces(a, b):
    '''
    Devuelve la sumatoria de un número a cierta cantidad b de veces.
    Pre: El primer parámetro acepta el número que se quiera sumar.
         El segundo parámetro acepta un número entero positivo. Representa el número de veces 
         que se desea sumar el número del primer parámetro.
    Pos: Devuelve el resultado de la sumatoria. Si el segundo parámetro recibido es 0, 
         devuelve 0.
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1   # Esta línea descuenta la cantidad de veces que resta iterar.
    return res
    # Esta función contiene dos invariables de ciclo: res y nb.


def collatz(n):
    '''
    Si el parámetro recibido es 1, esta función devuelve 1.
    Si el parámetro recibido es ditinto de uno,
    esta función produce un bucle infinito.
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res