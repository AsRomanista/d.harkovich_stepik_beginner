# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.
# На вход программе подается натуральное число n, а затем n различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел,
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

number = int(input())

new_list = []

for i in range(number):
    digit = int(input())
    new_list.append(digit)

new_list.remove(max(new_list))
new_list.remove(min(new_list))

print(*new_list, sep='\n')


