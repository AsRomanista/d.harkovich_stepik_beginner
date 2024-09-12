# На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом.
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.

name_surname = input()

surname = ''

for i in range(len(name_surname)):
    if name_surname[i] == ' ':
        surname += name_surname[i + 1]
if surname == surname.upper() and name_surname[0] == name_surname.upper()[0]:
    print('YES')
else:
    print('NO')

# вариант проще

s = input()

if s == s.title():
    print("YES")
else:
    print("NO")