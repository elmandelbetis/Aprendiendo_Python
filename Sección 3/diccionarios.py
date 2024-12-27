# -*- coding: utf-8 -*-

student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)