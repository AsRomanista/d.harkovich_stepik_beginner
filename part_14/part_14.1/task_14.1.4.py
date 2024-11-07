# Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник с основанием и высотой равными
# 15 и 8 соответственно:

def draw_triangle(height):
    for i in range(height):
        for j in range(height - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print('*', end='')
        print()

draw_triangle(8)