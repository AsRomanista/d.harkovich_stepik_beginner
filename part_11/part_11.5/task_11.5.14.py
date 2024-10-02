# На вход программе подается строка текста, содержащая 4 целых неотрицательных числа, разделенных точкой.
# Напишите программу, которая определяет, является ли введенная строка текста корректным ip-адресом.

ip = input()

list_ip_digits = ip.split('.')
count = 0

for i in range(len(list_ip_digits)):
    list_ip_digits[i] = int(list_ip_digits[i])
    if 0 <= list_ip_digits[i] <= 255:
        count += 1

if count == 4:
    print('YES')
else:
    print('NO')
