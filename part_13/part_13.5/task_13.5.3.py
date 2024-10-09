# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True,
# если число является простым, или False в противном случае.

def is_prime(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += 1
    if result == 2:
        return True
    else:
        return False

n = int(input())

print(is_prime(n))