# В службе по дорожному движению решили оптимизировать процесс создания автомобильных номеров:
# вместо человека генерацию автомобильных номеров поручили некоторой GPT (модели машинного обучения).
# Как мы знаем, искусственный интеллект ещё сыроват и делает много ошибок, поэтому его результаты следует тщательно проверять.

# Напишите программу, которая принимает на вход строку и проверяет, является ли эта строка корректным автомобильным номером.
# Программа должна вывести «YES» (без кавычек), если искусственный интеллект справился со своей задачей,
# или «NO» (без кавычек) в противном случае. В нашей задаче корректным автомобильным номером будем считать следующие форматы:

# <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
# <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>

# где <ЦИФРА> – это любая цифра, а <БУКВА> – это одна из букв кириллицы АВЕКМНОРСТУХ

auto_number = input()

letter = 'АВЕКМНОРСТУХ'

if (len(auto_number) == 9 and
        (auto_number[0] in letter) and
        (auto_number[1:4].isdigit()) and
        (auto_number[4] in letter) and
        (auto_number[5] in letter) and
        (auto_number[6] == '_') and
        ((auto_number[7:9]).isdigit())):
    print('YES')
elif (len(auto_number) == 10 and
        (auto_number[0] in letter) and
        (auto_number[1:4].isdigit()) and
        (auto_number[4] in letter) and
        (auto_number[5] in letter) and
        (auto_number[6] == '_') and
        ((auto_number[7:10]).isdigit())):
    print('YES')
else:
    print('NO')


