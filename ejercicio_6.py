# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:23:39 2023

@author: SEG
"""


### Ejercicio 6

class Persona:
    
        
    def __init__(self, nombre = None, edad = None, dni = None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    ## GETTERS ##
    
    @property # Getter de Nombre
    def nombre(self): 
        return self._nombre 
    
    @property # Getter de Edad
    def edad(self): 
        return self._edad 
    
    @property # Getter de DNI
    def dni(self): 
        return self._dni
    
    ## SETTERS ##
    def definir_nombre(self, name):
        
        ##No requiere validación
        
        self._nombre = name 
         
    def definir_edad(self, age):
        
        
        #Se valida que sea un número entero y menor que 115
        #(El hombre vivo más viejo tiene 114!)
        
        while type(age) != int or age >115:
            try:
                age = int(input('Ingrese un valor entero menor a 115: '))
            except:
                pass
        self._edad = age
        
    def definir_dni(self, numero_dni):
        
        #Se comprueba que sea un valor entero y menor a 99.999.999
        
        while type(numero_dni) != int or numero_dni>99999999:
            try:
                numero_dni = int(input('Ingrese el número de DNI sin puntos: '))
            except:
                pass
        self._dni = numero_dni
    
    def Es_mayor_de_edad(self):
        return self.edad>18
    
    def mostrar(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")
        print(f"DNI: {self._dni}")
    
    def __str__(self):
        return f"Nombre: {self._nombre} DNI: {self._dni}"

    def __repr__(self):
        return f"Nombre: {self._nombre} DNI: {self._dni}"

