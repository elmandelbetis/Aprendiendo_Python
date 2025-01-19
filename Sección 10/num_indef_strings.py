# -*- coding: utf-8 -*-
"""
Define a function that takes an indefinite number of strings as parameters and 
returns a list containing all the strings in UPPERCASE and sorted alphabetically.
"""

def mayus(*palabras):
    lista = [palabra.upper() for palabra in palabras]
    lista.sort()
    return lista


print(mayus("snow", "glacier", "iceberg"))