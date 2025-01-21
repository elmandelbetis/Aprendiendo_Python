# -*- coding: utf-8 -*-
"""
Define a function that takes as a parameter a list that contains both integers 
and strings and returns the list containing only the integers. For example, 
if I called your function with foo([99, 'no data', 95, 94, 'no data']) it 
should return [99, 95, 94].
"""

def foo(lista):
    new_lista = [el for el in lista if type(el) == int]
    return new_lista

l = [99, 'no data', 95, 94, 'no data']
print(foo(l))