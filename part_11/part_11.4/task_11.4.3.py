# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции f(x) - x ** 2 + 2 * x + 1,
# каждое на отдельной строке.
from string import digits

number = int(input())

new_list = []
fx_list = []

for i in range(number):
    digit = int(input())
    new_list.append(digit)
    fx_list.append(digit ** 2 + 2 * digit + 1)

print(*new_list, sep='\n')
print()
print(*fx_list, sep='\n')


