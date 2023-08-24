# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:23:39 2023

@author: SEG
"""

from funciones import mcd

### Ejercicio 2

valor_mcm1 = int(input('Ingrese un valor entero: ')) 
valor_mcm2 = int(input('Ingrese un otro entero: '))


mcm  = int(valor_mcm1 *valor_mcm2/mcd(valor_mcm1,valor_mcm2))

print(f'El mínimo común múltiplo es : {mcm}')