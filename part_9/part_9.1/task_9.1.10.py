# На вход программе подается одна строка состоящая из цифр.
# Напишите программу, которая считает сумму цифр данной строки.

string = input()
total = 0

# for i in range(len(string)):
#     total += int(string[i])
# print(total)

for i in string:
    total += int(i)
print(total)

