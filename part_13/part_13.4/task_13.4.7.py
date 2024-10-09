# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца
# и возвращает количество дней в данном месяце.

def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        result = 31
    elif month in [4, 6, 9, 11]:
        result = 30
    elif month == 2:
        result = 28
    return result


num = int(input())

print(get_days(num))