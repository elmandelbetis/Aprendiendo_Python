# -*- coding: utf-8 -*-
"""
Escribe un programa que pida al usuario un número entero y diga si es par o impar.
"""

def es_par(x):
    if x % 2 == 0:
        return True
    else:
        return False

#################################################################

num = int(input("Introduzca un número: "))

if es_par(num):
    print("El número es par")
else:
    print("El número es impar")

