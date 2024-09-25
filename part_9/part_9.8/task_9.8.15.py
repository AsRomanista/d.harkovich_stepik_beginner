# На вход программе подаются 3 различных слова.
# Вам необходимо отсортировать эти слова по возрастанию в лексикографическом порядке
# и вывести их на одной строке, разделяя символом пробела.

list_string = []

for i in range(3):
    string = input()
    list_string.append(string)

list_string = sorted(list_string)


print(*list_string)