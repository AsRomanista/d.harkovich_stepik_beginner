# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения:
# длину окружности и площадь круга, ограниченного данной окружностью.

import math

def get_circle(radius):
    circle_len = 2 * math.pi * radius
    circle_square = math.pi * radius ** 2
    return circle_len, circle_square


r = float(input())

length, square = get_circle(r)
print(length, square)