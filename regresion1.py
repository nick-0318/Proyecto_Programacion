#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 18:36:26 2021

@author: javiervivas
"""

import pandas as pd
import numpy as np

#revisar si es posible dejarla a un lado
def pregunta():
    numexp =  int(input("Ingrese el número de variables explicativas que desse para su modelo: ")) #El numero de variables explicativas
    empty = [] #lista vacia
    for i in range(numexp): #Le pregunta al usuario el nombre de las variables
        b = input("Por favor, ingrese el nombre de la variable explicativa: ")
        empty.append(b)
    print("Estas son las variables a considerar para su modelo: ", empty)

def estimarBetas (data, datax, datay):
    """Vamos a estimar las Betas de la regresión lineal, mediante el método de minimos cuadrados."""
    numexp =  int(input("Ingrese el número de variables explicativas que desse para su modelo: ")) #El numero de variables explicativas
    empty = [] #lista vacia
    for i in range(numexp): #Le pregunta al usuario el nombre de las variables
          b = input("Por favor, ingrese el nombre de la variable explicativa: ")
          empty.append(b)
    print("Estas son las variables a considerar para su modelo: ", empty)
    datax = [] #la matriz con nuestras variables explicativas
    for i in empty: #va agregando las variables explicativas a una matriz general x
        if i in data:
            datax.append(i) #las va agregando de una a una
        elif i not in data:
            print("Revisar si el nombre existe.")
    #mirar como usar esta matriz con la libreria pandas para poder multiplicarla 
    #Ahora que le pregunte al usuario cual variable quiere explicar
    empdep = []
    dep = input("Por favor, ingrese la variable a explicar: ")
    if dep in data:
        empdep.append(dep)
    else:
        print("Por favor revise si escribió bien el nombre de la variable.") #Revisar si se puede hacer con un error programable
    
    
    
