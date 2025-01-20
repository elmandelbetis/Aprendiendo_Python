# -*- coding: utf-8 -*-
"""
Comprueba si un número ingresado es primo o no. Además, 
encuentra todos los números primos entre 1 y uno introducido.
"""

import math

def es_primo(numero):
    for i in range (2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    
    return True


num = int(input("Inserte un número: "))

if es_primo(num):
    print("El número es primo")
else:
    print("El número no es primo")