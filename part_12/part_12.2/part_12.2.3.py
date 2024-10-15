# На вход программе подается строка текста, содержащая натуральные числа.
# Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.

string = input().split()

numbers = [int(num) for num in string]

string_list = ['+'.join(string)]

print(*string_list, '=', sum(numbers), sep='')