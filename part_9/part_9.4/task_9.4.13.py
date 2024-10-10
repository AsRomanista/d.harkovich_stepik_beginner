# На вход программе подаётся строка текста.
# Напишите программу, которая выводит на экран символ, который появляется наиболее часто.

string= input()

total = 0
total_symbol = ''

for i in string:
    if string.count(i) >= total:
        total = string.count(i)
        total_symbol = i

print(total_symbol)
