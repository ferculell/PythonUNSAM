import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.shape_base import tile

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
colors = ['#0048BA', '#B0BF1A', '#7CB9E8', '#B284BE', 
          '#C46210', '#E52B50', '#FFBF00', '#3B7A57', 
          '#3DDC84', '#87A96B', '#3D0C02', '#DA1884']
walks = []

# Generamos 12 caminatas aleatorias y las guardamos en la lista walks.
for i in range(12):
    walks.append(randomwalk(N))

# Guardamos los valores máximos de cada caminata generada.
max_val_in_walks = [max(abs(item)) for item in walks]

# Guardamos las posiciomes en walks de las caminatas con mayor y con menor valor máximo.
index_max = max_val_in_walks.index(max(max_val_in_walks))
index_min = max_val_in_walks.index(min(max_val_in_walks))

# Creamos el gráfico.
plt.figure(figsize=(14, 14))
for i in range(12):
    plt.subplot(2,1,1)
    plt.plot(walks[i], color=colors[i])
    plt.title('12 caminatas aleatorias')
    plt.xlabel('tiempo')
    plt.ylabel('distancia al origen')
    plt.ylim(-800, 800)
plt.subplot(2, 2, 3)
plt.plot(walks[index_max], color=colors[index_max])
plt.title('Caminata que más se aleja del origen')
plt.xlabel('tiempo')
plt.ylabel('distancia al origen')
plt.ylim(-800, 800)
plt.subplot(2, 2, 4)
plt.plot(walks[index_min], color=colors[index_min])
plt.title('Caminata que menos se aleja del origen')
plt.xlabel('tiempo')
plt.ylabel('distancia al origen')
plt.ylim(-800, 800)
plt.show()