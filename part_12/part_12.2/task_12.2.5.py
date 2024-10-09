# На вход программе подается строка текста.
# Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.

string = input().split()

list_max = [len(digit) for digit in string]

print(max(list_max))