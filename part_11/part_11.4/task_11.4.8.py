# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая сначала выводит все отрицательные числа, затем нули,
# а затем все положительные числа, каждое на отдельной строке.
# Числа должны быть выведены в том же порядке, в котором они были введены.

number = int(input())

new_list = []

for i in range(number):
    digit = int(input())
    new_list.append(digit)

new_sorted_list = []

for j in new_list:
    if j < 0:
        print(j)

for k in new_list:
    if k == 0:
        print(k)

for l in new_list:
    if l > 0:
        print(l)