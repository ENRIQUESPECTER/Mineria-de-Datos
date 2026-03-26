import numpy as np
from scipy import stats

#1. Datos: calificaciones registradas de los estudiantes
minutos = np.array([
    35,50,42,45,25,30,47,12,40,31,
    29,49.40,50,46,47,52,55,43,40,
    49,52,50,51,45
])

#2) El valor hipotetico de la media bajo H0
mu0 = 45

#3) Ejecuta la prueba t de 1 muestra
res = stats.ttest_1samp(minutos, mu0)#sintaxis para ttest_1samp: ttest_1samp(a,mu0) donde a es la muestra y mu0 es el valor bajo H0

#4) Extrae ek estadustuci t t ek p-value
t_stat = res.statistic
p_value = res.pvalue

#5) Valor de significancia (ALPHA)
alpha = 0.05

print("t =", t_stat)
print("p-value =",p_value)

if p_value < alpha:
    print("Rechaza H0: hay evidencia de que la media es distinta de 45.")
else:
    print("No rechaza H0: No hay evidencia suficiente que demuestre que la media difiere de 45.")