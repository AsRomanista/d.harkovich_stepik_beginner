# На вход программе подается строка текста,
# содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.

string = input()

split_words = string.split()


for i in split_words:
    print(i[0], end='.')