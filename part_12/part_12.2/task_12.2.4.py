# На вход программе подается строка текста.
# Напишите программу, которая определяет, является ли введенная строка корректным телефонным номером.
# Строка текста является корректным телефонным номером, если она имеет формат:
# abc-def-hijk или
# 7-abc-def-hijk,
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9

string = input().split('-')

if string[0] == '7':
    del string[0]

if len(string) == 3 and \
        string[0].isdigit() and len(string[0]) == 3 and \
        string[1].isdigit() and len(string[1]) == 3 and \
        string[2].isdigit() and len(string[2]) == 4:
    print('YES')
else:
    print('NO')