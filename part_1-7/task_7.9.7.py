# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит все простые числа от a до b включительно

num_1, num_2 = int(input()), int(input())

for i in range(num_1, num_2 + 1):
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


# the second variant without flags:
num_1, num_2 = int(input()), int(input())


for i in range(num_1, num_2 + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)