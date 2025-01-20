# -*- coding: utf-8 -*-

with open("bear.txt") as archivo:
    contenido = archivo.read()

print(contenido[:90])