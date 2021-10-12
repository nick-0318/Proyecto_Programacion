# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:28:28 2021

@author: nicol
"""

import regresion1

print("Bienvenido, este es un set de herramientas que le ayudaran a realizar regresiones lineales, junto con herramientas estadisticas que otorgan elementos analiticos adicionales para lasd regresiones lineales")
print("A continuación ingresara las caracteristicas del modelo que desea correr.")
regresion1.pregunta()
print("Tiene 4 funciones integradas en este set de herramientasas de regresión: \n1-Test de normalidad. \n2-Calcular los parametros beta por el método de minimos cuadrados ordinarios. \n3-Calcular el R^2, poder explicativo de las variables. \n4-Graficar el modelo de regresión lineal")
opcion=input("Ingrese el número de la opción que desea ejecutar: ")
if opcion==1:
    regresion1.test_normalidad()
if opcion==2:
    regresion1.estimarBetas()
if opcion==3:
    regresion1.poder_explicativo()
if opcion==4:
    regresion1.graficar()
avanzar=input("Desea realizar alguna otra acción(Y/N): ")
    