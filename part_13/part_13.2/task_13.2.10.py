# Напишите функцию print_digit_sum(),
# которая принимает одно натуральное число num и выводит на печать сумму его цифр.

def print_digit_sum(num):
    total = 0
    for i in str(num):
        total += int(i)
    print(total)

n = int(input())

print_digit_sum(n)