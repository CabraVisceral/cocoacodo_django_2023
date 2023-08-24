# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:23:09 2023

@author: SEG
"""

### EJERCICIO 7

class Cuenta():
    def __init__(self, titular, cantidad=0):
        self._titular = titular
        self._cantidad = cantidad
    
    ## GETTERS ##

    @property # Getter de Nombre
    def titular(self): 
        return self._titular 
    
    @property # Getter de Nombre
    def cantidad(self): 
        return self._cantidad 
    
    ## SETTERS ##
    
    def definir_nombre(self, persona):            
        self._titular = persona
        
    def ingresar(self, dinero):
        try:
            dinero = int(dinero)
            if dinero > 0:          
                self._cantidad += int(dinero)
                print(f"Total: {self._cantidad}")
        except:
            pass
        
    def retirar(self, dinero):          
        
        try:
            dinero = int(dinero)    
            self._cantidad -= dinero
            print(f"Total: {self._cantidad}")
        except:
            pass

    