# -*- coding: utf-8 -*-
"""
Define a function that takes as parameter list of numbers and returns the list 
containing only the numbers that are greater than 0. For example, I called your
 function with foo([-5, 3, -1, 101]) it should return [3, 101].
"""


def foo(lista):
    positivos = [num for num in lista if num > 0]
    return positivos
    

lista_numeros = [-5, 3, -1, 101]
print(foo(lista_numeros))