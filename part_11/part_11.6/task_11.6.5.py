# Дополните приведённый ниже код, чтобы он:
# Заменил второй (по порядку) элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый (по порядку) элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список с помощью функции print()

numbers = [8, 9, 10, 11]

numbers[1] = 17

new_list = [4, 5, 6]
numbers.extend(new_list)

numbers.pop(0)

numbers_copy = numbers.copy()
numbers.extend(numbers_copy)

numbers.insert(3, 25)

print(numbers)
