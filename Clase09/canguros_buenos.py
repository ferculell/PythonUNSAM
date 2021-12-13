class Canguro:
    def __init__(self, nombre, lista=None):
        self.nombre = nombre
        self.contenido_marsupio = lista or []  # si no se pasa un parámetro para lista se inicializa con una lista vacía
    
    def __str__(self):
        return f'{self.nombre}: {self.contenido_marsupio}'

    def meter_en_marsupio(self, algo):
        self.contenido_marsupio.append(algo)



"""Este código continene un 
bug importante y dificil de ver
"""

# class Canguro:
#     """Un Canguro es un marsupial. Esta clase contenía un bug en su constructor, ya que
#     inicializaba la misma lista para todas las instancias de la clase que utilizaban el 
#     valor por omisión del parámetro contenido.
#     """

#     def __init__(self, nombre, contenido=None):
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         self.contenido_marsupio = contenido or []  ### El error se soluciona inicializando la lista vacía en esta línea

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)