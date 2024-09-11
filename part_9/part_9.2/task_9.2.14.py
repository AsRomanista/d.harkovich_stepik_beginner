# На вход программе подается строка текста.
# Напишите программу, которая разрежет ее на две равные части, переставит их местами и выведет на экран.

string = input()
lenght = int(len(string))

if lenght % 2 == 0:
    first_half = string[:(int(lenght / 2))]
    second_half = string[(int(lenght / 2)):]
    print(second_half + first_half)
else:
    first_half = string[:(int(lenght // 2) + 1)]
    second_half = string[(int(lenght // 2) + 1):]
    print(second_half + first_half)

