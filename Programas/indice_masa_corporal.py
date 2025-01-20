# -*- coding: utf-8 -*-
"""
Solicita el peso y la altura del usuario y calcula su IMC, indicando si está 
en un rango saludable.
"""

def calcular_indice_masa(peso, altura):
    return peso / ((altura / 100)**2)

def determinar_salud(indice_masa):
    if indice_masa < 18.5:
        print("Usted tiene un índice de masa corporal BAJO")
    elif indice_masa >= 18.5 and indice_masa <= 24.9:
        print("Usted tiene un índice de masa corporal NORMAL")
    elif indice_masa > 25 and indice_masa < 29.9:
        print("Usted tiene SOBREPESO")
    else:
        print("Usted tiene OBESIDAD")


p = float(input("Introduzca peso (en kilogramos): "))
a = float(input("Introduzca altura (en centímetros): "))
print("\n")

imc = calcular_indice_masa(p, a)

print(f"El índice de masa corporal es {imc}")
determinar_salud(imc)
