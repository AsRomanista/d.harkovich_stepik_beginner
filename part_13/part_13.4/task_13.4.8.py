# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число
# и возвращающую список всех делителей данного числа.

def get_factors(num):
    result = [divisor for divisor in range(1, num + 1) if num % divisor == 0]
    return result

n = int(input())

print(get_factors(n))