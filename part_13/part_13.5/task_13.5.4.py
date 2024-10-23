# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число большее числа num

# from task_13.5.3
def is_prime(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += 1
    if result == 2:
        return True
    else:
        return False

# --------

def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

n = int(input())

print(get_next_prime(n))