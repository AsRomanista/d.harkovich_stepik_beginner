# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит все простые числа от a до b включительно

a, b = int(input()), int(input())

for i in range(a, b + 1):
    flag = True
    if i < 2:
        flag = False
    else:
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
    if flag:
        print(i)