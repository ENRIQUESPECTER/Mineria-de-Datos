import numpy as np
from scipy import stats

#1. Datos: Perdida de peso en kg de las personas
GrupoA = np.array([
    10,5,9,14,12,15,12,9,11,8,
    8,12,15,14,11,14,9,12,8,10,
    13,12,9,14,14,15,14,11,7,9
])

GrupoB = np.array([
    7,5,6,9,3,8,10,3,12,11,
    6,11,8,6,8,10,9,8,5,4,
    10,5,9,10,11,5,8,9,5,7
])

#2) Ejecuta la prueba t de 1 muestra
res = stats.ttest_ind(GrupoA,GrupoB, equal_var=False)#sintaxis para ttest_1samp: ttest_1samp(a,mu0) donde a es la muestra y mu0 es el valor bajo H0

#3) Extrae el estadistico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

#4) Valor de significancia (ALPHA)
alpha = 0.05

print("t =", t_stat)
print("p-value =",p_value)

if p_value < alpha:
    print("Rechaza H0: hay evidencia de que existe diferencia signficativa entre los programas por 3 meses.")
else:
    print("No rechaza H0: No hay evidencia suficiente que demuestre que existe diferencia significativa entre los programas por 3 meses.")