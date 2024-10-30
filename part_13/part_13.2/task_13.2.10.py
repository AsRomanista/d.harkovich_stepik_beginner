# Напишите функцию print_digit_sum(),
# которая принимает одно натуральное число num и выводит на печать сумму его цифр.

def print_digit_sum(num):
    digit_sum = sum(int(i) for i in str(num))
    print(digit_sum)

n = int(input())

print_digit_sum(n)