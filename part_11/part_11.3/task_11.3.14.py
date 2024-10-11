# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает список из символов всех строк, а затем выводит его.

number = int(input())
list_string = []

for i in range(number):
    list_string.extend(input())

print(list_string)