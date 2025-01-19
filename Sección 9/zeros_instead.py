# -*- coding: utf-8 -*-
"""
Define a function that takes as parameter a list that contains both numbers 
and strings and returns the same list but with zeros instead of strings. For 
example, I called your function with foo([99, 'no data', 95, 94, 'no data']) 
it should return [99, 0, 95, 94, 0].
"""

def foo(lista):
    aux = [el if type(el) == int or type(el) == float else 0 for el in lista]
    return aux


li = [99, 'no data', 95, 94, 'no data']
print(foo(li))