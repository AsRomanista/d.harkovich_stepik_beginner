# Магическая дата – это дата, когда день, умноженный на месяц, равен числу, образованному последними двумя цифрами года.
# Напишите функцию is_magic(date), которая принимает в качестве аргумента строковое представление корректной даты
# и возвращает значение True, если дата является магической и False - в противном случае.

def is_magic(date):
    date_list = date.split('.')
    date = int(date_list[0])
    month = int(date_list[1])
    year = int(date_list[2][-2:])
    if date * month == year:
        return True
    else:
        return False

date = input()

print(is_magic(date))
