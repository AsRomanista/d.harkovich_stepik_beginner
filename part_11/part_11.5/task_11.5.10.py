# На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.

string = input()

print(*string.split(), sep='\n')