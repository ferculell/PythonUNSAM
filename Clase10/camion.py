class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __repr__(self):
        return f'Camion({self.lotes})'

    def __str__(self):
        acumulador = ''
        for lote in self.lotes:
            acumulador += f'\nLote de {lote.cajones} cajones de {lote.nombre}, pagados a ${lote.precio} cada uno.'
        return f'Camión con {len(self.lotes)} lotes:{acumulador}'

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def __len__(self):
        return len(self.lotes)

    def __getitem__(self, i):
        return self.lotes[i]

    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total