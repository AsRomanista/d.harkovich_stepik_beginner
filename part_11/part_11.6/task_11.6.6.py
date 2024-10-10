# На вход программе подается строка текста, содержащая различные натуральные числа.
# Вам необходимо переставить максимальный и минимальный элементы местами и вывести измененную строку.

digits = input()

digits_list = []

for digit in digits.split():
    digits_list.append(int(digit))


max_digit = digits_list.index(max(digits_list))
min_digit = digits_list.index(min(digits_list))


digits_list[max_digit], digits_list[min_digit] = digits_list[min_digit], digits_list[max_digit]

print(*digits_list)