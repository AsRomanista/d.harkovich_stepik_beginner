# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

number = int(input())

new_list = []

for i in range(number):
    string = input()
    if string not in new_list:
        new_list.append(string)

print(*new_list, sep='\n')
