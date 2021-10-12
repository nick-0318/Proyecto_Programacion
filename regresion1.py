#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 18:36:26 2021

@author: javiervivas
"""

import pandas as pd
import numpy as np


def pregunta():
    numexp =  int(input("Ingrese el número de variables explicativas que desse para su modelo: ")) #El numero de variables explicativas
    empty = [] #lista vacia
    for i in range(numexp): #Le pregunta al usuario el nombre de las variables
        b = input("Por favor, ingrese el nombre de la variable explicativa: ")
        empty.append(b)
    print("Estas son las variables a considerar para su modelo: ", empty)

def estimarBetas (data, datax, datay):
    """Vamos a estimar las Betas de la regresión lineal, mediante el método de minimos cuadrados."""
    pregunta()
    
    
    

estimarBetas(1, 2, 3)
    