# -*- coding: utf-8 -*-
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
    

# Ejemplo de user input
user_input = int(input("Enter temperature: ")) # Cast heredado de C 
print(weather_condition(user_input))   
