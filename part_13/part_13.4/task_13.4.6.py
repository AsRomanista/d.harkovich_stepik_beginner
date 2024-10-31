# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях.
# Формула для преобразования: мили = километры * 0.6214.

def convert_to_miles(km):
    return round(km * 0.6214, 4)

num = int(input())

print(convert_to_miles(num))