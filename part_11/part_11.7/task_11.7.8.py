# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, использующую списочное выражение, которая выведет кубы указанных чисел также на одной строке.

string = input().split()

list_number = [int(digit) ** 3 for digit in string]

print(*list_number)