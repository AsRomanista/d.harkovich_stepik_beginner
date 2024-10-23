# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа
# a, b, c – коэффициенты квадратного уравнения a * x ** 2 + b * x + c = 0 и возвращает его корни в порядке возрастания.

from math import *

def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return  min(x1, x2), max(x1, x2)
    elif d == 0:
        x1 = -b / (2 * a)
        return x1, x1
    elif d < 0:
        print('Нет корней')

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)