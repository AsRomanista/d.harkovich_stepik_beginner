# Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка
# (x1; y1) и (x2; y2) и возвращает координаты точки являющейся серединой данного отрезка.

def get_middle_point(x1, y1, x2, y2):
    x_len = (x1 + x2) / 2
    y_len = (y1 + y2) / 2
    return x_len, y_len

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)