# -*- coding: utf-8 -*-

import time
import os

while True:
    if os.path.exits("../files/vegetables.txt"):
        with open("../files/vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)