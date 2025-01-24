# -*- coding: utf-8 -*-
"""
El legado de Fibonacci
"CON EL PODER DEL BALONCESTO (-ESTOO) (-ESTOOOO)!!!!" - Mr Jägger
"""

def fibonacci(termino):
    
    # Casos base
    if termino == 0:
        return 0
    elif termino == 1:
        return 1
    
    # Caso recursivo
    return fibonacci(termino - 1) + fibonacci(termino - 2)



# Programa principal

n = int(input("Introduzca el término f(n) a calcular de la sucesión: "))
print(f"El valor de la sucesión de Fibonacci para f({n}) es: {fibonacci(n)}")
    

