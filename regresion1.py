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

#Opcion 1 del set (Estamos trabajando en ello)
def testnormalidad():
    input("Ingrese el tipo de test que desea realizar: ")


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
    #--mirar como usar esta matriz con la libreria pandas para poder multiplicarla.
    #--No se como hacer esto ... omg ... mira si puedes tu
    #Ahora que le pregunte al usuario cual variable quiere explicar
    empdep = []
    dep = input("Por favor, ingrese la variable a explicar: ")
    if dep in data:
        empdep.append(dep)
    else:
        print("Por favor revise si escribió bien el nombre de la variable.") #R--evisar si se puede hacer con un error programable
    
def rsquared (datax, datay, df):
    """Va a hallar el R^2. Recibe la variable dependiente y las independientes."""
    #En si r^2 lo podemos definir como R^2= 1-SSR/SST
    df = len(datay)-len(datax)-1 # los grados de libertad
    yhat = np.p(datax)                         #lo usaremos para que nos haga el fit
    ybar = np.sum(datay)/len(datay)  #metodo provisonal, mirar que tal funciona
    ssr = np.sum((yhat-ybar)**2)   # a ssr lo podemos definir como la sumatoria de errores al cuadrado
    sst = np.sum((datay-ybar)**2)     # a sst lo podemos definir como sse + ssr
    r2 = 1 - (ssr /sst)
    adr2 = 1-(1-r2)*(len(datay-1))/(df) #el r^2 ajustado
    return r2, adr2 #revisar muy bien que esto tenga sentido alguno

def poder_explicativo():
    None
#Opcion 4 del set (Revisar opciones para graficar regresiones linelaes)
def graficar():
    None
