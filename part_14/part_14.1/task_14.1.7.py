# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num
# и возвращает его словесное описание на русском языке.

def number_to_words(num):
    list_num = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    list_num_10 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                   'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_num_20 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    if num <= 10:
        for i in str(num):
            i = int(i)
            result = list_num[i - 1]
    elif 10 < num <= 19:
        for i in str(num):
            i = int(i)
            result = list_num_10[i - 1]
    elif num >= 20:
        first = num // 10
        second = num % 10
        if second > 0:
            result = list_num_20[first - 2] + ' ' + list_num[second - 1]
        else:
            result = list_num_20[first - 2]

    return result


n = int(input())

print(number_to_words(n))
