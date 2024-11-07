# Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en
# и number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.

def get_month(language, number):
    mon_ru = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
              "декабрь"]

    mon_en = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]
    if language == 'ru':
        result = mon_ru[number - 1]
    elif language == 'en':
        result = mon_en[number - 1]
    return result

lan = input()
num = int(input())

print(get_month(lan, num))