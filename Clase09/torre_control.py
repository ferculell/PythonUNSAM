class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


class TorreDeControl:
    '''
    Representa el funcionamiento de una torre de control de vuelos.
    Maneja el orden de asignación de pista mediante objetos instanciados de la clase Cola.
    '''
    def __init__(self):
        self.lista_arribo = Cola()
        self.lista_partida = Cola()

    def nuevo_arribo(self, arribo):
        self.lista_arribo.encolar(arribo)

    def nueva_partida(self, partida):
        self.lista_partida.encolar(partida)

    def ver_estado(self):
        if self.lista_arribo.esta_vacia():
            print('No hay vuelos esperando para aterrizar.')
        else:
            print(f'Vuelos esperando para aterrizar: {", ".join(item for item in self.lista_arribo.items)}')
        if self.lista_partida.esta_vacia():
            print('No hay vuelos esperando para despegar.')
        else:
            print(f'Vuelos esperando para despegar: {", ".join(item for item in self.lista_partida.items)}')

    def asignar_pista(self):
        if self.lista_arribo.esta_vacia():
            if self.lista_partida.esta_vacia():
                print('No hay vuelos en espera.')
            else:
                vuelo = self.lista_partida.desencolar()
                print(f'El vuelo {vuelo} despegó con éxito.')
        else:
            vuelo = self.lista_arribo.desencolar()
            print(f'El vuelo {vuelo} aterrizó con éxito.')