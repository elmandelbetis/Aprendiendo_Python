# -*- coding: utf-8 -*-

monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures)

monday_temperatures.append(8.1)
print(monday_temperatures)

monday_temperatures.__getitem__(1)

monday_temperatures.clear()
print(monday_temperatures)

cool_list = ['H', 'e', 'l', 'l', 'o']
cool_string = str.join("", cool_list)
print(cool_string)
cool_string = str.join("---", cool_list)
print(cool_string)