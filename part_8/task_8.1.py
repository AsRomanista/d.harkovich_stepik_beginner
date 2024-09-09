# На обработку поступает натуральное число.
# Нужно написать программу, которая выводит на экран сумму четных цифр этого числа или 0,
# если четных цифр в записи нет. Программист торопился и написал программу неправильно.

n = int(input())
total = 0

while n != 0:
    first_num = n % 10 # check first number
    if first_num % 2 == 0 or first_num == 0: # check division by 2 and 0 value
        total += first_num
    n //= 10
print(total)