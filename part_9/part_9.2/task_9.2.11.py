# На вход программе подается одно слово, записанное в нижнем регистре.
# Напишите программу, которая определяет, является ли оно палиндромом.

string = input()

if string[:] == string[::-1]:
    print("YES")
else:
    print("NO")
