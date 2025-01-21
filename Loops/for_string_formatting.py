# -*- coding: utf-8 -*-
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has a phone number {pair[1]}")
    
for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")