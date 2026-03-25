import numpy as np
import scipy.stats as stats
import pandas as pd
     

#Datos del problema
mu_0 = 1000 #Hipotesis nula
n = 40 #Tamano de la prueba
x_bar = 990 #Media muestral
s = 12 #Desviacion estandar muestral
alpha = 0.02 #Nivel de significancia
     

#Calculo del estadistico de prueba z
z = (x_bar - mu_0) / (s/np.sqrt(n))
     

#Valor critico para la prueba
z_critical = stats.norm.ppf(1-alpha)
     

#Comparacion de los valores
if z > z_critical:
    print("Rechazo la hipotesis nula")
else:
  print("No rechazar la hipotesis nula")

#Crear un dataframe con los datos
df = pd.DataFrame({
    'Parametros': ['Media Teorica', 'Media Muestral', 'Desviacion Estandar', 'Tamano de la muestra', 'Z-calculado', 'Z-critico', 'Conclusion'],
    'valores': [mu_0, x_bar, s, n, z, z_critical, 'Rechazar la hipotesis nula' if z >z_critical else 'No rechazar la hipotesis nula']
})

print(df)