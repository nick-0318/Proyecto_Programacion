#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:05:00 2021

@author: javiervivas
"""

import pandas as pd

database = input("Nombre de la base de datos (Incluya el '.csv'): ")
delimitar = input("Formato en la que está delimitado (',', ';', etc): ")

data = pd.read_csv(database, delimiter= delimitar)
header = data.columns
print(header)

variable = int(input("¿Cuántas variables explicativas tiene el modelo?: "))


vari = []
exp = []
for i in range(variable):
    variablex = input("¿Cuáles son variables explicativas tiene el modelo?: ")
    if variablex in header:
        vari.append(variablex)
        exp.append(data[variablex])
    else:
        print("No existe.")

print(vari)
print(variablex)
    

