# На вход программе подается строка, содержащая английский текст.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

string = input().lower()

string_list = string.split()

a = string_list.count('a')
an = string_list.count('an')
the = string_list.count('the')

print('Общее количество артиклей:', (a + an + the))