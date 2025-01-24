# -*- coding: utf-8 -*-
"""
El legado de Fibonacci
"CON EL PODER DEL BALONCESTO (-ESTOO) (-ESTOOOO)!!!!" - Mr Jägger
"""
import time


def fibonacci_lineal(termino):
    # Casos base
    if termino == 0:
        return 0
    elif termino == 1:
        return 1
    
    a = 0
    b = 1

    for i in range (2, n+1):
        a, b = b, a + b
    
    return b
    
def fibonacci_recursivo(termino):
    
    # Casos base
    if termino == 0:
        return 0
    elif termino == 1:
        return 1
    
    # Caso recursivo
    return fibonacci_recursivo(termino - 1) + fibonacci_recursivo(termino - 2)



# Programa principal

n = int(input("Introduzca el término f(n) a calcular de la sucesión: "))

start = time.time()
print(f"Fibonacci f({n}) lineal: {fibonacci_lineal(n)}")
end = time.time()
print(f"Tiempo transcurrido: {end - start} segundos")


start = time.time()
print(f"Fibonacci f({n}) recursivo: {fibonacci_recursivo(n)}")
end = time.time()
print(f"Tiempo transcurrido: {end - start} segundos")


