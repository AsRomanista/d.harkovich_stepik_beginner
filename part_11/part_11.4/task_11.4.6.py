# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

number = int(input())

new_list = []

for i in range(number):
    string = input()
    new_list.append(string)

search_string = input().lower()

for j in new_list:
    if search_string in j.lower():
        print(j)
