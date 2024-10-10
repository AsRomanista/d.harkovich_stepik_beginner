# На вход программе подается натуральное число
# n, а затем n строк. Напишите программу, которая создает из указанных строк список и выводит его.

number = int(input())

list_string = []

for i in range(number):
    string = input()
    list_string.append(string)

print(list_string)