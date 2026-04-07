import numpy as np
from scipy import stats

#EJERCICIO NUMERO 1
#Tabla de frecuanciaas observadas
print("EJERCICIO NUMERO 1\n")
tabla = np.array([
    [85,65],
    [50,100]
])
chi2, p_value, gl, esperados = stats.chi2_contingency(tabla, correction=False)
#Imprimir los resultados
print(f"Chi Cuadrado = {chi2}")
print(f"P_value = {p_value}")
print(f"Grados de Libertad = {gl}")
print(f"Frecuencias Esperadas = {esperados}")
print(esperados)

alpha = 0.05

if p_value < alpha:
    print("Existe evidenvia de que hay relacion entre la ciudad y la preferencia de transporte\n")
else:
    print("No existe evidenvia de que hay relacion entre la ciudad y la preferencia de transporte\n")


#EJERCICIO NUMERO 2
#Tabla de frecuanciaas observadas
print("EJERCICIO NUMERO 2\n")
tabla = np.array([
    [40,20],
    [35,45],
    [15,45]
])
chi2, p_value, gl, esperados = stats.chi2_contingency(tabla, correction=False)
#Imprimir los resultados
print(f"Chi Cuadrado = {chi2}")
print(f"P_value = {p_value}")
print(f"Grados de Libertad = {gl}")
print(f"Frecuencias Esperadas = {esperados}")
print(esperados)

alpha = 0.05

if p_value < alpha:
    print("Existe evidenvia de que hay relacion entre el nivel educativo y el habito de fumar\n")
else:
    print("No existe evidenvia de que hay relacion entre el nivel educativo y el habito de fumar\n")



#EJERCICIO NUMERO 3
#Tabla de frecuanciaas observadas
print("EJERCICIO NUMERO 3\n")
tabla = np.array([
    [10,50],
    [30,40],
    [45,5]
])
chi2, p_value, gl, esperados = stats.chi2_contingency(tabla, correction=False)
#Imprimir los resultados
print(f"Chi Cuadrado = {chi2}")
print(f"P_value = {p_value}")
print(f"Grados de Libertad = {gl}")
print(f"Frecuencias Esperadas = {esperados}")
print(esperados)

alpha = 0.05

if p_value < alpha:
    print("Existe evidenvia de que hay relacion entre el tipo de dieta y el nivel de colesterol")
else:
    print("No existe evidenvia de que hay relacion entre el tipo de dieta y el nivel de colesterol")