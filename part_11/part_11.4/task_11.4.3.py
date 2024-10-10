# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая для каждого введенного числа x выводит значение функции f(x) - x ** 2 + 2 * x + 1,
# каждое на отдельной строке.

number = int(input())

new_list = []

for _ in range(number):
    digit = int(input())
    new_list.append(digit)

print(*new_list, sep='\n')
print()

for i in range(len(new_list)):
    j = (int(new_list[i]) ** 2 + 2 * int(new_list[i]) + 1)
    print(j, sep='\n')


