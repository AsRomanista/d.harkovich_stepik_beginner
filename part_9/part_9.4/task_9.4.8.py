# На вход программе подаётся строка текста, состоящая из слов, разделённых ровно одним пробелом.
# Напишите программу, которая подсчитывает количество слов в ней.

string = input()

space = string.count(' ')

print(space + 1)