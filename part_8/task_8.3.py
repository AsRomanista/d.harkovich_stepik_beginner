# На обработку поступает последовательность из 4 целых чисел.
# Известно, что вводимые числа по абсолютной величине не превышают 10**8.
# Нужно написать программу, которая выводит на экран количество нечетных чисел в исходной последовательности
# и максимальное нечетное число.
# Если нечетных чисел нет, требуется на экран вывести «NO».
# Программист торопился и написал программу неправильно.

n = 4
count = 0
maximum = -10**8

for i in range(n):
    num = int(input())
    if num % 2 != 0:
        count += 1
        if num > maximum:
            maximum = num
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')