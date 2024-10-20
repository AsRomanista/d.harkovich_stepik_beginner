# В школе BEEGEEK названия учебных классов необычные. Они имеют следующий формат:
# <номер класса><буква класса>
# где <номер класса> должен находиться в диапазоне от 0 (как и все у программистов) до 9 включительно,
# а буквой класса могут быть все буквы в диапазоне от «А» до «П» включительно.
# Напишите программу, которая принимает натуральное число
# n, а далее n названий классов, каждое на новой строке.
# Для каждого названия класса ваша программа должна выводить на отдельной строке «YES» (без кавычек),
# если название класса корректное, или «NO» (без кавычек) в противном случае.

numbers = int(input())
letters = 'АБВГДЕЖЗИЙКЛМНОП'

for i in range(numbers):
    class_name = input()
    if len(class_name) == 2 and class_name[0].isdigit() and class_name[1] in letters:
        print('YES')
    else:
        print('NO')
