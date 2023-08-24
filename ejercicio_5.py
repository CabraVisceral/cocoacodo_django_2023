# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:23:39 2023

@author: SEG
"""


### Ejercicio 5
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia)

def get_int(): #FUNCIÓN RECURSIVA
    try:
        valor = int(input('Ingrese un valor entero: '))
    except ValueError:
        print('El valor ingresado es incorrecto. ', end='')
        valor = get_int()
    
    return valor

def get_int2(): #FUNCIÓN ITERATIVA
    
    valor = ValueError
    try:
        valor = int(input('Ingrese un valor entero: '))
    except ValueError:
        while valor == ValueError:
            try:
                valor = int(input('El valor ingresado es incorrecto. Ingrese un valor entero: '))
            except ValueError:
                pass
    return valor
