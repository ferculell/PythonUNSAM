import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')

df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][['altura_tot', 'diametro']].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][['altura_arbol', 'diametro_altura_pecho']].copy()

df_tipas_parques.rename(columns={'altura_tot': 'altura'}, inplace=True)
df_tipas_veredas.rename(columns={'altura_arbol': 'altura', 'diametro_altura_pecho': 'diametro'}, inplace=True)

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

f, axs = plt.subplots(1, 2, figsize=(12, 6))
sns.boxplot(x='ambiente', y='diametro', data=df_tipas, ax=axs[0])
sns.boxplot(x='ambiente', y='altura', data=df_tipas, ax=axs[1])
f.tight_layout()
plt.show()