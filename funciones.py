# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:16:43 2023

@author: SEG
"""

def mcd(valor1,valor2):
    mayor = max(valor1,valor2)
    menor = min(valor1,valor2)
    resultado = menor
    
    if mayor%menor != 0:
        resultado = mcd(menor, mayor%menor)  
    return resultado

def str_a_dict(parrafo):
    lista_palabras =  parrafo.lower().split()
    diccionario_palabras = {}
    for palabra in lista_palabras:
        diccionario_palabras[palabra] = lista_palabras.count(palabra)
    return diccionario_palabras
def tupla_palabra_mas_frecuente(diccionario):
    palabra = max(diccionario, key=diccionario.get)
    return  [palabra, diccionario[palabra]]