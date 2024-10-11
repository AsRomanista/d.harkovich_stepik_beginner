# На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке).
# Напишите программу, которая выводит инициалы человека.

name = input()
surname = input()
patronymic = input()

print(surname[0] + name[0] + patronymic[0])

# via 'for'

initials = ''

for i in range(3):
    if i == 0:
        initials += surname[0]
    elif i == 1:
        initials += name[0]
    elif i == 2:
        initials += patronymic[0]

print(initials)