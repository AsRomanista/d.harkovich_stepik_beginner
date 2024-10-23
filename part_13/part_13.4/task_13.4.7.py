# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца
# и возвращает количество дней в данном месяце.

def get_days(month):
    if month in [2]:
        result = 28
    elif month in [4, 6, 9, 11]:
        result = 30
    else:
        result = 31
    return result


num = int(input())

print(get_days(num))