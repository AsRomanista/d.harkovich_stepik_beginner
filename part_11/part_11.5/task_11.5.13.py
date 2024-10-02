# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, которая по заданным числам строит столбчатую диаграмму.

string = input()

digits_list = string.split()

for i in range(len(digits_list)):
    digits_list[i] = int(digits_list[i])
    print('+' * digits_list[i])