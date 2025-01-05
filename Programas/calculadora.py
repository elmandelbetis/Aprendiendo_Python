# -*- coding: utf-8 -*-
"""
Crea un programa que solicite al usuario dos números y una operación 
(suma, resta, multiplicación, división). Realiza la operación seleccionada 
y muestra el resultado. Maneja errores como división por cero.
"""

def suma(x1, x2):
    return x1 + x2


def resta(x1, x2):
    return x1 - x2


def multiplicacion(x1, x2):
    return x1 * x2


def division(x1, x2):
    if x2 == 0:
        return "ERROR: no se puede dividir por cero"
    else:
        return x1 / x2
 
#################################################################    

FIN = 'F'
res = 0     # resultado acumulado
car = ''
num1 = float(input("Introduzca un número: "))
num2 = float(input("Introduzca otro número: "))


while car != FIN:
    car = input("Introduzca S (Sumar), R (Restar), M (Multiplicar), D (Dividir): ")
    
    if car == 'S':
        res = suma(num1, num2)
        print(res)
        num2 = float(input("Introduzca otro número: "))
    
    elif car == 'R':
        res = resta(num1, num2)
        print(res)
        num2 = float(input("Introduzca otro número: "))
    
    elif car == 'M':
        res = multiplicacion(num1, num2)
        print(res)
        num2 = float(input("Introduzca otro número: "))
    
    elif car == 'D':
        res = division(num1, num2)
        print(res)
        num2 = float(input("Introduzca otro número: "))
    
    elif car == 'F':
        print("Saliendo...")
    
    else:
        print("Por favor, introduzca los caracteres S, R, M, D o F")
    




