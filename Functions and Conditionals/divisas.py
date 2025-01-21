# -*- coding: utf-8 -*-

# Función que convierte a una divisa asumiendo que vale x1,75 de la otra
def convert(amount):
    output = amount * 1.75
    return output


print(convert(10))