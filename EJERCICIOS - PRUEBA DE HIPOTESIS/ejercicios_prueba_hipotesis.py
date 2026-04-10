import numpy as np
from scipy import stats

print("EJERCICIO NUMERO 1")
print("Es t-student de 1 muestra\n")

botellas = np.array([498, 501, 499, 502, 500, 497, 503, 499, 501, 500])
mu0 = 10

res = stats.ttest_1samp(botellas, mu0)

t_stat = res.statistic
p_value = res.pvalue

alpha = 0.05
print(f"t = {t_stat}")
print(f"Valor p = {p_value}")

if p_value < alpha:
    print("Rechaza H0: hay evidencia de que la media es distinta de 500.\n")
else:
    print("No rechaza H0: No hay evidencia suficiente que demuestre que la media difiere de 500.\n")


print("EJERCICIO NUMERO 2")
print("Es t-student 2 muestras \n")

musica = np.array([65, 70, 68, 72, 66, 69, 71, 67, 70, 68])
silencio = np.array([85, 88, 90, 87, 92, 86, 89, 91, 88, 90])

res2 = stats.ttest_ind(musica, silencio, equal_var=False)

t_stat2 = res2.statistic
p_value2 = res2.pvalue

alpha = 0.01
print(f"t = {t_stat2}")
print(f"Valor de p = {p_value2}")

if p_value2 < alpha:
    print("Existe diferencia entre las calificaciones finales entre estudiantes que estudian con musica y en silencio\n")
else:
    print("No existe diferencia entre las calificaciones finales entre estudiantes que estudian con musica y en silencio\n")

print("EJERCICIO NUMERO 3")
print("Es chi-cuadrado prueba de Bondad Ajuste \n")

observadas = np.array([200,120,80])
p = np.array([0.40,0.35,0.25])

n = observadas.sum()
# 4. Calcular las Frecuencias esperadas
esperadas = n * p

# 5. Calculo del estadistico chi-cuadrado
res = stats.chisquare(f_obs= observadas, f_exp = esperadas)

# 6. Extraer los resultados
chi2 = res.statistic
p_value = res.pvalue
gl = len(observadas) - 1 

# 7. Mostrar resultados
print(f"Frecuencias observadas: {observadas}")
print(f"Frecuencias esperadas: {esperadas}")
print(f"Chi cuadrado: {chi2:.4f}")
print(f"Grados de Libertad: {gl}")
print(f"Valor p: {p_value:.4f}")

alpha = 0.05
 
if p_value < alpha:
    print("Se rechaza la hipotesis nula")
else: 
    print("No se rechaza la hipotesis nula")