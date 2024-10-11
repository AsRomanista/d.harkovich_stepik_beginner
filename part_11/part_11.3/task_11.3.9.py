# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список их кубов.

number = int(input())
list_cube = []

for i in range(number):
    digits = int(input())

    list_cube.append(digits ** 3)

print(list_cube)