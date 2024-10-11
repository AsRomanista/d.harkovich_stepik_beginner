# Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди.
# На приёмник ему поступает n различных последовательностей кода Морзе.
# Декодировав их, он получает последовательности из цифр и букв строчного латинского алфавита.
# При этом только в сообщениях Оди содержится число 11, причём минимум 3 раза.
# Помогите определить Джиму количество сообщений от Оди.

n = int(input()) # message number
total_messages = 0

for i in range(n):
    string = input()
    if string.count('11') >= 3:
        total_messages += 1
print(total_messages)
