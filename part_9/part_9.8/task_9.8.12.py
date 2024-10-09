# В некотором наборе слов Сэм находит "волшебное" число по следующему алгоритму:
# берет самую "маленькую" и самую "большую" строки, перемножает Unicode-коды последних символов этих строк и
# возводит полученное число в квадрат. Результатом и является "волшебное" число.
# На вход программе подаются 4 слова. Найдите "волшебное" число в этом наборе слов.

string1, string2, string3, string4 = input(), input(), input(), input()

max_string = max(string1, string2, string3, string4)
min_string = min(string1, string2, string3, string4)
max_number = ord(max_string[-1])
min_number = ord(min_string[-1])
print((max_number * min_number) ** 2)


