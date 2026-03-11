import pandas as pd
import numpy as np
from numpy import random

#Tipos de array

array_cero = np.array(5)
print(array_cero)

array_1 = np.array([1,2,3,4,5,6])
print(array_1)

array_2 = np.array([[1,2,3], [4,5,6]])
print(array_2)

array_3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(array_3)

#Indez de los arrays
print(array_1[0])
print(array_3[0][1][1])
print(array_3[1][0][0])

#Shape
print(array_1.shape)
print(array_2.shape)
print(array_3.shape)

print(array_1.reshape(1,6))
print(array_2.reshape(3,2))
print(array_3.reshape(2,3,2))

#Concatenacion
print("CONCATENAR ARRAYS")
print(np.concatenate((array_1, array_1)))

#Separacion
print("SEPARAR ARRAYS")
print(np.split(array_1, 2))

#where
print("DONDE SE ENCUENTRA UN NUMERO")
print(np.where(array_1 == 3))

#ordenacion
print("CONCATENACION")
arraynew = np.array([10,50,2,0,7,9])
print(np.sort(arraynew))
print(np.sort(arraynew)[::-1])

#random
print("FUNCION DE RANDOM CON ENTEROS")
numero = random.randint(100,200,1) #(inicio, fin, num_elementos)
print(numero)

numero = random.randint(10,size=(5))
print(numero)

numero = random.randint(10,size=(2,3))
print(numero)

#numeros decimales
print("FUNCION RANDOM CON DECIMALES")
numero = random.rand()
print(round(numero,2))

numero2 = random.rand() + 5
print(numero2)

numero3 = random.rand(3,5)
print(numero3)

#listas
print("LISTA Y CHOICE")
lista_nombre = ["Juan","Pedro","Maria"]
print(random.choice(lista_nombre))

#EJERCICIOS
print("\nEJERCICIOS DE NUMPY\n")
print("Ejercicio 1")
diez_numeros = random.randint(100,size=(10))
print(diez_numeros)
print("Ejercicio 2")
cinco_numeros = random.rand(1,5)
print(cinco_numeros)
print("Ejercicio 3")
array1 = random.randint(10,size=(5))
array2 = random.randint(10,size=(5))
print(np.concatenate((array1,array2)))
print("Ejercicio 4")
array_10 = random.randint(0,10,10)
print(np.split(array_10, 2))
print("Ejercicio 5")
matriz = random.rand(3,3)
print(matriz)
print("Ejercicio 6")
array_azar = random.randint(10,size=(10))
print(random.choice(array_azar,3))
print("Ejercicio 7")
array_media = random.randint(100)
print(np.mean(array_media))
