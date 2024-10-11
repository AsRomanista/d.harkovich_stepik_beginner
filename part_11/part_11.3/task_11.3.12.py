# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список,
# затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

number = int(input())
list_digits = []

for i in range(number):
    digits = int(input())
    list_digits.append(digits)

del list_digits[1::2]

print(list_digits)