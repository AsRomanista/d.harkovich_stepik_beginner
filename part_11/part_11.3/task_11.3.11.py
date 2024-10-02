# На вход программе подается натуральное число n, где n≥2. Затем поступают n целых чисел.
# Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д)
from itertools import count

number = int(input())

list_number = []

for i in range(number):
    digits = int(input())
    list_number.append(digits)

sum_list_number = []

for j in range(len(list_number) - 1):
    sum_list_number.append(list_number[j] + list_number[j + 1])

print(sum_list_number)