# -*- coding: utf-8 -*-
"""
Define a function that takes as parameter a list that contains decimal numbers 
as strings and returns the sum of those numbers. For example, I called your 
function with foo(['1.2', '2.6', '3.3']) it should return 7.1. Note that the 
floats of the input list are string datatypes.
"""

def foo(lista):
    return sum([float(el) for el in lista])
    
li = ['1.2', '2.6', '3.3']
print(foo(li))