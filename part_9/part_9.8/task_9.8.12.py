# В некотором наборе слов Сэм находит "волшебное" число по следующему алгоритму:
# берет самую "маленькую" и самую "большую" строки, перемножает Unicode-коды последних символов этих строк и
# возводит полученное число в квадрат. Результатом и является "волшебное" число.
# На вход программе подаются 4 слова. Найдите "волшебное" число в этом наборе слов.

list_string = []

for i in range(4):
    string = input()
    list_string.append(string)

if list_string:
    max_string = max(list_string)
    min_string = min(list_string)
    max_number = ord(max_string[-1])
    min_number = ord(min_string[-1])
    print((max_number * min_number) ** 2)
