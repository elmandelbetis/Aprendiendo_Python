# -*- coding: utf-8 -*-
"""
Convierte una cantidad de una moneda (por ejemplo, dólares) a otra (como euros),
según una tasa ingresada por el usuario.
"""

lista_divisas = ["Dolar", "Euro", "Yuan", "Yen", "Libra"]
abreviaturas = ["USD", "EUR", "CNY", "JPY", "GBP"]

tasas_conversion = {
    "Dolar": {"Euro": 0.97, "Yuan": 7.31, "Yen": 155.91, "Libra": 0.82},
    "Euro": {"Dolar": 1.04, "Yuan": 7.57, "Yen": 161.39, "Libra": 0.85},
    "Yuan": {"Dólar": 0.14, "Euro": 0.13, "Yen": 21.31, "Libra": 0.11},
    "Yen": {"Dolar": 0.0064, "Euro": 0.0062, "Yuan": 0.047, "Libra": 0.0052},
    "Libra": {"Dolar": 1.22, "Euro": 1.18, "Yuan": 8.95, "Yen": 190.74}
}


def obtener_abreviatura(moneda):
    try:
        indice = lista_divisas.index(moneda)
        return abreviaturas[indice]
    except ValueError:
        return None


def convertir_moneda(moneda_origen, moneda_destino, cantidad):
    if moneda_origen in tasas_conversion and moneda_destino in tasas_conversion[moneda_origen]:
        tasa = tasas_conversion[moneda_origen][moneda_destino]
        return cantidad * tasa
    else:
        return None
    


# Mostrar lista de divisas disponibles
print("Monedas disponibles: ", ", ".join(lista_divisas))


# Entrada del usuario
origen = input("Introduce la moneda de origen: ").capitalize()
destino = input("Introduce la moneda destino: ").capitalize()
dinero = float(input("Introduce la cantidad de dinero a cambiar: "))
print("")


# Obtener abreviaturas
abreviatura_origen = obtener_abreviatura(origen)
abreviatura_destino = obtener_abreviatura(destino)


# Verificar que las monedas sean válidas
if abreviatura_origen and abreviatura_destino:
    resultado = convertir_moneda(origen, destino, dinero)
    if resultado is not None:
        print(f"{dinero:.2f} {abreviatura_origen} son {resultado:.2f} {abreviatura_destino}.")
    else:
        print("La conversión de las divisas introducidas no está disponible.")

else:
    print("Moneda no válida. Por favor, revisa las opciones disponibles")
    


