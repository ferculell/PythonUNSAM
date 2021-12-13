import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('../Data/temperaturas.npy')

plt.hist(temperaturas, bins=20)
plt.show
