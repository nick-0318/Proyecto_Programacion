#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:05:00 2021
@author: javiervivas
"""

import pandas as pd
import numpy as np
import matplotlib as plt

database = input("Nombre de la base de datos (Incluya el '.csv'): ") #pregunta el nombre de la base
delimitar = input("Formato en la que está delimitado (',', ';', etc): ")

data = pd.read_csv(database, delimiter= delimitar)
header = data.columns
print(header)
cuantanas = data.isnull().sum().sum()
print ('Cantidad de NaN (O variables vacias): ', cuantanas)
data = data.fillna(0) #para arreglar los nans, reemplaza por 0

daty = []
variabledep = input("¿Cuál es la variable dependiente que tiene el modelo?: ")
data1 = daty.append(data[[variabledep]])
datay = np.array(daty) 
print(datay)

variable = int(input("¿Cuántas variables explicativas tiene el modelo?: "))

#extrae los datos de la base de datos
vari = []
exp = []
for i in range(variable):
    variablex = input("¿Cuáles son variables explicativas tiene el modelo?: ")
    if variablex in header:
        vari.append(variablex)
        exp.append(data[variablex])
    else:
        print("No existe.")

print(exp)
# Crea una matriz vacia
w, h = variable+1, len(exp[1])
Matrix = [[0 for x in range(w)] for y in range(h)] 

#crear el vector de unos y los añade 
for i in range(len(exp[1])):
    Matrix[i][0] = 1
Matrix

#completamos la matriz con los datos 
for i in range(variable):
    for n in range(len(exp[1])):
        for t in exp[i[1]]: #revisar esto
            Matrix[n][1] = t
            
Matrix

#convierte esa matriz en un array comun y corriente
A = np.array(Matrix)
A

#halla la transpuesta de esa matriz
At = np.transpose(A)
At

#Multiplica a A con At
AAt = np.dot(A,At)
AAt  

#halla la inversa de la matriz

Ai = np.linalg.inv(AAt)
Ai

#Multiplicamos nuevamente Ai con At
y1 = np.dot(Ai, At)

#finalmente, la regresion sería
y = np.dot(y1, datay)

#grafica:
plt.plot(y)
plt.show()

#los errores del modelo
u = np.subtract(datay, y) 
print(u)
