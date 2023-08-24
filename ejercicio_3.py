# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:23:39 2023

@author: SEG
"""

from funciones import str_a_dict

### Ejercicio 3
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia)

texto = input('''Ingrese un texto, se creará un diccionario con las 
    palabras que aparezcan y la cantidad de veces: \n''')
diccionario_de_palabras = str_a_dict(texto)

print("Diccionario: ", diccionario_de_palabras)
