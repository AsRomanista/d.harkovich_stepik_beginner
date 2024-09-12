# На вход программе подается строка.
# Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.

string = input()
lower_case = 0

for i in range(len(string)):
    if string[i] != string.upper()[i]:
        lower_case += 1

print(lower_case)