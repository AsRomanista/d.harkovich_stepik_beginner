# На вход программе подается одна строка.
# Напишите программу, которая выводит в столбик элементы строки в обратном порядке.

string = input()

for i in range(-1, -(len(string) + 1), -1):
    print(string[i])