# На вход программе подается строка текста.
# Напишите программу, которая определяет, является ли введенная строка корректным телефонным номером.
# Строка текста является корректным телефонным номером, если она имеет формат:
# abc-def-hijk или
# 7-abc-def-hijk,
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9

string = input().split('-')

length = [len(i) for i in string]

if length == [3, 3, 4] and ''.join(string).isdigit():
    print('YES')
elif length == [1, 3, 3, 4] and ''.join(string).isdigit() and string[0] == '7':
    print('YES')
else:
    print('NO')