# Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и
# возвращает значение биномиального коэффициента, равного n! / k! * (n - k)!

import math

def compute_binom(n, k):
    total = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return round(total)

n = int(input())
k = int(input())

print(compute_binom(n, k))