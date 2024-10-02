# На вход программе подается натуральное число n и n строк, а затем число k.
# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

number = int(input())
list_string = []

for i in range(number):
    list_string.append(input())

k_index = int(input())

for j in list_string:
    if k_index <= len(j):
        print(j[k_index - 1], end='')



