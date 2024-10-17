# Подключите модуль random;
# Создайте строковые константы:
# digits: 0123456789;
# lowercase_letters: abcdefghijklmnopqrstuvwxyz;
# uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
# punctuation: !#$%&*+-=?@^_.
# Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

# Программа должна запрашивать у пользователя следующую информацию:
# Количество паролей для генерации;
# Длину одного пароля;
# Включать ли цифры 0123456789?
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
# Включать ли символы !#$%&*+-=?@^_?
# Исключать ли неоднозначные символы il1Lo0O?

question_quantity_passwords = int(input('Какое количество паролей для генерации? '))
length = int(input('Какая длина пароля? '))
question_digits = input('Включать ли цифры 0123456789? (y = yes, n = no) ').lower()
question_upper_letter = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y = yes, n = no) ').lower()
question_lower_letter = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y = yes, n = no) ').lower()
question_punctuation = input('Включать ли символы !#$%&*+-=?@^_? (y = yes, n = no) ').lower()
question_ambiguous_symbols = input('Исключать ли неоднозначные символы il1Lo0O? (y = yes, n = no) ').lower()

# На основании введенной пользователем информации, сформируйте переменную chars,
# содержащую все символы, которые могут быть в генерируемом пароле.

if question_digits == 'y':
    chars += digits
if question_upper_letter == 'y':
    chars += uppercase_letters
if question_lower_letter == 'y':
    chars += lowercase_letters
if question_punctuation == 'y':
    chars += punctuation
if question_ambiguous_symbols == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

# Напишите функцию generate_password(), которая принимает два аргумента:
# length: длину пароля;
# chars: алфавит из символов которого состоит пароль;
# и возвращает пароль.
# Используя цикл for, сгенерируйте необходимое количество паролей.

def generate_password(chars, length):
    return random.sample(chars, length)

for j in range(question_quantity_passwords):
    print(*generate_password(chars, length), sep='')





