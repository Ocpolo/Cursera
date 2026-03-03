print("Hola Mundo") 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns       

#Leer el dataset de Ecoplas
df_ecoplas = pd.read_csv(r"C:/Users/Oiden/OneDrive - Universidad Nacional Abierta y a Distancia/Documents/Dataset/ecoplas.csv")

#Imprimir las primeras filas del dataset, la información general y la forma del dataframe
print(df_ecoplas.head(10))
print(df_ecoplas.info())

