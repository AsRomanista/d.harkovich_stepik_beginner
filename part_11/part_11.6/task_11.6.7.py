# На вход программе подается строка, содержащая английский текст.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

string = input().lower()

string_list = string.split()

a = int(string_list.count('a'))
an = int(string_list.count('an'))
the = int(string_list.count('the'))

print('Total number of articles:', (a + an + the))