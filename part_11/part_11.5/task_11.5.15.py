# На вход программе подается строка текста и строка-разделитель.
# Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста.

string, separator = input(), input()

list_string = []

for i in string:
    list_string.append(i)

print(separator.join(list_string))