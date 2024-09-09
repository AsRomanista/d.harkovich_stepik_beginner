# Дано натуральное число. Напишите программу, которая вычисляет:
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречаются цифры 0 и 5 (всего суммарно).

n = int(input())

num_3 = 0
last_digit_score = 0
even_digit_score = 0
more_5_score = 0
more_7_score = 1
score_0_5 = 0

last_digit = n % 10



while n > 0:
    current_digit = n % 10
    if current_digit == 3:
        num_3 += 1
    if  current_digit == last_digit:
        last_digit_score += 1
    if current_digit % 2 == 0:
        even_digit_score += 1
    if current_digit > 5:
        more_5_score += current_digit
    if current_digit > 7:
        more_7_score *= current_digit
    if current_digit == 0 or current_digit == 5:
        score_0_5 += 1
    n //= 10


print(num_3)
print(last_digit_score)
print(even_digit_score)
print(more_5_score)
print(more_7_score)
print(score_0_5)