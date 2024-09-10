# На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления.

number = int(input())
binary_number = ''

while number > 0:
    new_number = number % 2
    binary_number = str(new_number) + binary_number
    number //= 2

print(binary_number)


