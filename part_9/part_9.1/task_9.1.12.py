# На вход программе подается одна строка.
# Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *.

string = input()
total_plus = 0
total_mult = 0

for i in range(len(string)):
    if string[i] == '+':
        total_plus += 1
    if string[i] == '*':
        total_mult += 1

print('Символ + встречается', total_plus, 'раз')
print('Символ * встречается', total_mult, 'раз')

