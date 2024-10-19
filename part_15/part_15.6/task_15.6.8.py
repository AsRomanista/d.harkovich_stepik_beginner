# Переведите десятичное число 513 в двоичную систему счисления.

number, result = int(input()), ''

while number > 0:
    result += str(number % 2)
    number //= 2
print(result[::-1])