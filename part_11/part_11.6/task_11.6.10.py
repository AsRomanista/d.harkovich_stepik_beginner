# На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел.
# Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.
digit_list = []


for i in input().split():
    digit_list.append(int(i))

digit_list.sort()
print(*digit_list)
digit_list.sort(reverse=True)
print(*digit_list)



