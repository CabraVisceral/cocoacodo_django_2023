# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:23:39 2023

@author: SEG
"""

from funciones import str_a_dict, tupla_palabra_mas_frecuente
### Ejercicio 3

texto = input('''Ingrese un texto, se creará un diccionario con las 
    palabras que aparezcan y la cantidad de veces: \n''')
diccionario_de_palabras = str_a_dict(texto)

palabra_mas_frecuente = tupla_palabra_mas_frecuente(diccionario_de_palabras)
print(f'''Tupla con la palabra que más aparece y su frecuencia: 
      {palabra_mas_frecuente}''')
