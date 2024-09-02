# def filter_string(text, symbol):
#     symbol_lower = symbol.lower()
#     result = ''
#     for char in text:
#         if char.lower() != symbol_lower:
#             result += char
#     return result.strip()
#
# text = 'I look back if you are lost'
# print(filter_string(text, 'I'))

# def is_palindrome(text):
#     if text.lower() == text[::-1].lower():
#         return True
#     return False
#
# print(is_palindrome('ишак ищет у тещи каши'))

# def count_vowels(text):
#     vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
#
# print(count_vowels('One'))

# print('31', sep='+')
# print('31', end='-')

# number = int(input())
# first = number // 10 ** (5-1) % 10
# second = number // 10 ** (5-2) % 10
# third = number // 10 ** (5-3) % 10
# fourth = number // 10 ** (5-4) % 10
# fifth = number // 10 ** (5-5) % 10
# print(first, second, third, fourth, fifth)

# a = int(input())
# aa = 10 * a + a
# aaa = 100 * a + 10 * a + a
# print(aaa + aa + a)

# a = 7 // 8
# b = 7 % 8
# print(b)

# num = int(input())
# first = num // 10 ** (4-1) % 10
# second = num // 10 ** (4-2) % 10
# third = num // 10 ** (4-3) % 10
# fourth = num // 10 ** (4-4) % 10
# if first + fourth == second - third:
#     print('ДА')
# else:
#     print('НЕТ')

# year = int(input())
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print('YES')
# else:
#     print('NO')

# параллельность прямых
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if y1 == y2 or x1 == x2:
#     print('YES')
# else:
#     print('NO')

# ход королём
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
#     print('YES')
# else:
#     print('NO')

# определить треугольник (равносторонний, разносторонний,  равнобедренный)
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a == b or a == c or b == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# определить срединной значение
# a = int(input())
# b = int(input())
# c = int(input())
# if (b < a < c) or (c < a < b):
#     print(a)
# elif (a < b < c) or (c < b < a):
#     print(b)
# else:
#     print(c)

# a = int(input())
# b = int(input())
# c = input()
# if c == '/' and b != 0:
#     print(a / b)
# elif c == '*':
#     print(a * b)
# elif c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif b == 0 and c == '/':
#     print('На ноль делить нельзя!')
# else:
#     print('Неверная операция')

# найти пересечение отрезков
# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# start = max(a1, a2)
# end = min(b1, b2)
# if start == end:
#     print(start)
# elif start > end:
#     print('пустое множество')
# elif start < end:
#     print(start, end)

# заканчивается ли число на 00
# num = int(input())
# if num % 100 == 0:
#     print('YES')
# else:
#     print('NO')

# # покрашены ли шахматные клетки в один цвет
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if (x1 + y1) % 2 == (x2 + y2) % 2:
#     print('YES')
# else:
#     print('NO')

# age = int(input())
# sex = input()
# if 10 <= age <= 15 and sex == 'f':
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# if 1 <= num <= 10 and num == 1:
#     print('I')
# elif 1 <= num <= 10 and num == 2:
#     print('II')
# elif 1 <= num <= 10 and num == 3:
#     print('III')
# elif 1 <= num <= 10 and num == 4:
#     print('IV')
# elif 1 <= num <= 10 and num == 5:
#     print('V')
# elif 1 <= num <= 10 and num == 6:
#     print('VI')
# elif 1 <= num <= 10 and num == 7:
#     print('VII')
# elif 1 <= num <= 10 and num == 8:
#     print('VIII')
# elif 1 <= num <= 10 and num == 9:
#     print('IX')
# elif 1 <= num <= 10 and num == 10:
#     print('X')
# else:
#     print('ошибка')

# ход слона
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if abs(x2 - x1) == abs(y2 - y1):
#     print('YES')
# else:
#     print('NO')

# ход коня
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if abs(x2 - x1) == 2 and abs(y2 - y1) == 1:
#     print('YES')
# elif abs(x2 - x1) == 1 and abs(y2 - y1) == 2:
#     print('YES')
# else:
#     print('NO')

# ход ферзя
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if (x1 == x2 or y1 == y2) or abs(x1 - x2) == abs(y2 - y1):
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# num1 = num // 10 ** (3 - 1) % 10
# num2 = num // 10 ** (3 - 2) % 10
# num3 = num // 10 ** (3 - 3) % 10
# max1 = max(num1, num2, num3)
# min1 = min(num1, num2, num3)
# number_3 = abs(max1 + min1 - num1 - num2 - num3)
#
# if max1 - min1 == number_3:
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# доказать что длина трёхх строк явл арифметической прогрессией
# string1 = input()
# string2 = input()
# string3 = input()
#
# max_leght = max(len(string1), len(string2), len(string3))
# min_lenght = min(len(string1), len(string2), len(string3))
# avg_leght = len(string1) + len(string2) + len(string3) - max_leght - min_lenght
#
# if 2 * avg_leght == min_lenght + max_leght:
#     print('YES')
# else:
#     print('NO')

# from math import sqrt
#
# a = float(input())
# b = float(input())
#
# arithmetical_mean = (a + b) / 2
# geometric_mean = sqrt(a * b)
# harmonic_mean = 2 * a * b / (a + b)
# mean_square = sqrt((a ** 2 + b ** 2) / 2)

# print(arithmetical_mean, geometric_mean, harmonic_mean, mean_square, sep='\n')

# вычисление корней квадратного уравнения
# from math import *
#
# a = float(input())
# b = float(input())
# c = float(input())
#
# d = b ** 2 - 4 * a * c
#
# if d > 0:
#     x1 = (-b + sqrt(d)) / (2 * a)
#     x2 = (-b - sqrt(d)) / (2 * a)
#     print(min(x1, x2), max(x1, x2), sep='\n')
# elif d == 0:
#     x1 = -b / (2 * a)
#     print(x1)
# elif d < 0:
#     print('Нет корней')

# Напишите программу, которая предсказывает размер популяции организмов с 1-го по n-й день (включительно).
# Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.

# m = int(input())
# p = int(input())
# n = int(input())
#
# for i in range(n):
#     print(i + 1, m * ((1 + p / 100) ** i))

# Даны два целых числа m и n. Напишите программу, которая выводит все целые числа от m до n включительно в порядке возрастания,
# если m<n, или в порядке убывания в противном случае.

# m, n = int(input()), int(input())
#
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# elif m >= n:
#     for i in range(m, n - 1, -1):
#         print(i)

# Даны два целых числа m и n (m > n).
# Напишите программу, которая выводит все нечетные целые числа от m до n (включительно) в порядке убывания.
# m, n = int(input()), int(input())
#
# if m % 2 == 0:
#     m -= 1  # Если m четное, уменьшаем на 1, чтобы начать с ближайшего нечетного
#
# for i in range(m, n - 1, -2):
#     print(i)

# m, n = int(input()), int(input())
#
# for i in range(m, n + 1):
#     if i % 17 == 0 or (i % 3 == 0 and i % 5 == 0) or i % 10 == 9:
#         print(i)

# таблица умножения
# n = int(input())
#
# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)

# написать кол-во чисел куб которых закнчивает на 4 и 9
# m, n = int(input()), int(input())
# counter = 0
# for i in range(m, n + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         counter += 1
# print(counter)

# сумма 5 чисел
# n = int(input())
# score = 0
#
# for i in range(n):
#     number = int(input())
#     score = score + number
# print(score)

# расчёт формулы
# import math
#
# n = int(input())
# score = 0
#
# for i in range(1, n + 1):
#     score = score + 1 / i
#
# print(score - math.log(n))

# посчитать сумму чисел квадрат которых заканчивается на 2, 5 или 8

# n = int(input())
#
# score = 0
#
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         score = score + i
# print(score)

# вычислить произведение чисел отлично от 0
# score = 1
#
# for i in range(1, 11):
#     num = int(input())
#     if num != 0:
#         score = score * num
# print(score)

# сумма делителей числа без остатка
# n = int(input())
#
# score = 0
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         score = score + i
#
# print(score)

# написать сумму знакочередующей суммы
# n = int(input())
#
# score = 0
#
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         score += i
#     else:
#         score -= i
# print(score)


# найти максимальное значение и след. макс. значение
# n = int(input())
# max1 = None
# max2 = None
#
# for i in range(1, n + 1):
#     num = int(input())
#     if max1 is None or num > max1:
#         max2 = max1
#         max1 = num
#     elif max2 is None or num > max2:
#         max2 = num
#
#
# print(max1, max2, sep='\n')

# если все четные вывести - YES, если хотя бы одно нечетное то NO
# flag = 'YES'
#
# for i in range(1, 11):
#     num = int(input())
#     if num % 2 != 0:
#         flag = 'NO'
#
# if num % 2 == 0:
#     print(flag)
# else:
#     flag == 'NO'
#     print(flag)

# Фибоначчи
# n = int(input())
# a, b = 1, 1
#
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# text = input()
# total = 0
# while not (text == 'стоп' or text == 'хватит' or text == 'достаточно'):
#     total += 1
#     text = input()
# print(total)

# num = int(input())
# total = 0
# while num >= 0:
#     total += num
#     num = int(input())
# print(total)

# вывести последовательность 5, по порядку, до отрицательного числа или больше 5
# num = int(input())
# score = 0
#
# while num > 0 and num <= 5:
#     if num == 5:
#         score += 1
#     num = int(input())
# print(score)

# num = int(input())
# score = 0

# Цикл продолжается, пока num больше 0
# while num > 0:
#     if num >= 25:
#         num -= 25
#     elif num >= 10:
#         num -= 10
#     elif num >= 5:
#         num -= 5
#     else:
#         num -= 1
#     score += 1  # Увеличиваем счетчик на каждой итерации
#
# print(score)

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# натуральное число в обратном порядке каждое число на новой строке

# num = int(input())
#
# new_num = 0
#
# while num != 0:
#     new_num = num % 10
#     print(new_num)
#     num = num // 10

# число наоборот
# num = int(input())
#
# new_num = 0
#
# while num != 0:
#     new_num = num % 10
#     print(new_num, end='')
#     num = num // 10

# найти максимальное и минимальное значение
# num = int(input())
# mx_num = 0
# mn_num = 9
#
# while num != 0:
#     last_number = num % 10
#     if last_number < mn_num:
#         mn_num = last_number
#     if last_number > mx_num:
#         mx_num = last_number
#     num = num // 10
#
# print('Максимальная цифра равна', mx_num)
# print('Минимальная цифра равна', mn_num)

# есть число и надо вычислить разные операции с его цифрами

# num = int(input())
# sum_num = 0
# lenght_num = 0
# mult_num = 1
# avg_num = 0
# original_num = num
# last_num = num % 10
#
# while num != 0:
#     sum_num += num % 10
#     lenght_num += len(str(num % 10))
#     mult_num *= num % 10
#     avg_num = sum_num / int(lenght_num)
#     num = num // 10
#
# first_num = original_num
# while first_num >= 10:
#     first_num = first_num // 10
#
# sum_last_first = first_num + last_num
#
# print(sum_num)
# print(lenght_num)
# print(mult_num)
# print(avg_num)
# print(first_num)
# print(sum_last_first)
# num = int(input())
#
# while num >= 100:
#     num = num // 10
#
# num_second = num % 10
# print(num_second)

# все ли цифры в числе одинаковые или нет
# num = int(input())
# count = 0
# last_number = num % 10
#
# while num != 0:
#     last_number_new = num % 10
#     num = num // 10
#     if last_number != last_number_new:
#         count += 1
#
# if count > 0:
#     print('NO')
# else:
#     print('YES')

# Напишите программу, которая определяет,
# является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

# num = int(input())
# last_num = num % 10
# flag = 'YES'
#
# while num > 0:
#     num = num // 10
#     if num > 0:
#         last_num_new = num % 10
#         if last_num > last_num_new:
#             flag = 'NO'
#         last_num = last_num_new
#
# print(flag)

# На вход программе подается число n > 1. Напишите программу, которая выводит его наименьший отличный от 1 делитель

# n = int(input())
#
# for i in range(2, n+1):
#     if n % i == 0:
#         print(i)
#         break

# вывести подряд числа за исключением определенных

# n = int(input())
#
# for i in range(1, n+1):
#     if 5 <= i <= 9:
#         continue
#     if 17 <= i <= 37:
#         continue
#     if 78 <= i <= 87:
#         continue
#     print(i)


# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n //= 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# печатаем сумму из промежутка с вложенными циклами
# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()

# вводим нечетное основание и делаем равнобедренный треугольник
# n = int(input())
#
# for i in range(1, n // 2 + 2):
#     print('*' * i)
# for i in range(n // 2, 0, -1):
#     print('*' * i)

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:

# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end="")
#     print()

# Решите уравнение в натуральных числах 28n+30k+31m=365

# total = 0
#
# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m)

# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка – 10 рублей, за корову –
# 5 рублей, за теленка – 0.5 рубля и надо купить 100 голов скота?

# total = 0
#
# for b in range(1, 11): # бык
#     for k in range(1, 21): # корова
#         for c in range(1, 201): # теленок
#             if 10 * b + 5 * k + 0.5 * c == 100: # and b + k + c == 100
#                 total += 1
#                 if b + c + k == 100:
#                     print('b =', b, 'k =', k, 'c =', c)

# опровержение гипотезы Эйлера

# total = 0

# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
#                 e = int(sum ** (1 / 5))
#                 if sum == e ** 5:
#                     print(a, b, c, d, e)
#                     print(a + b + c + d + e)
#                     break

# сделать треугольник с вершиной равной длиной введенного числа
# n = int(input())
# total = 0
#
# for i in range(1, n + 1):
#     for j in range(i):
#         total += 1
#         print(total, end=' ')
#     print()

# n = int(input())
#
#
# for i in range(1, n + 1):
#     for j in range(1, i * 2):
#         print(i - abs(i - j), end='')
#     print()

# найти максимальное число делителей, и вывести число с максимальной суммой делителей
# a, b = int(input()), int(input())
#
# max_sum_divisors = 0
# max_num = a
#
# for i in range(a, b + 1):
#     current_sum = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             current_sum += j
#     if current_sum > max_sum_divisors:
#         max_sum_divisors = current_sum
#         max_num = i
#     elif current_sum == max_sum_divisors:
#         if i > max_num:
#             max_num = i
#
# print(max_num, max_sum_divisors)

# вывести число i и кол-во ее делителей в виде +
# n = int(input())
#
# for i in range(1, n + 1):
#     current_sum = 0
#     print(i, end='')
#     for j in range(1, n + 1):
#         if i % j == 0:
#             current_sum += j
#             print('+', end='')
#     print()

# получить цифровой корень числа n
# n = int(input())
#
#
# while n > 9:
#     total = 0
#     while n > 0:
#         last_number = n % 10
#         total += last_number
#         n //= 10
#     n = total
# print(n)


# найти сумму факториалов
# from math import factorial

# n = int(input())
#
# # print(factorial(n))
# total = 1
# sum = 0
#
# for i in range(1, n + 1):
#     total *= i
#     sum += total
# print(sum)

