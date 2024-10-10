# На вход программе подается натуральное число n.
# Напишите программу, которая создает список, состоящий из делителей введенного числа.

number = int(input())
list_divider = []

for i in range(1, number + 1):
    if number % i == 0:
        list_divider.append(i)

print(list_divider)
