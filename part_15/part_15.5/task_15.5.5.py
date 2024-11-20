# Зашифруйте приведённый ниже текст алгоритмом Цезаря со сдвигом вправо на 10 символов:
# Блажен, кто верует, тепло ему на свете!
# Примечание. Считайте, что русский алфавит состоит из 32 букв (буква ё отсутствует).

def cyrillic_shift(num_shift):
    text = 'Блажен, кто верует, тепло ему на свете!'
    new_string = ''
    alphabet_length = 32

    # for i in text:
    #     if i.isalpha():
    #         if i.isupper():
    #             if (ord(i) + num_shift) <= ord('Я'):
    #                 new_string += chr(ord(i) + num_shift)
    #             else:
    #                 new_string += chr(ord(i) + num_shift - 32) # 32 - quantity of cyrillic characters without 'Ё'
    #         else:
    #             if (ord(i) + num_shift) <= ord('я'):
    #                 new_string += chr(ord(i) + num_shift)
    #             else:
    #                 new_string += chr(ord(i) + num_shift - 32) # 32 - quantity of cyrillic characters without 'Ё'
    #     else:
    #         new_string += i

    for char in text:
        if 'А' <= char <= 'Я':
            new_string += chr((ord(char) - ord('А') + num_shift) % alphabet_length + ord('А'))
        elif 'а' <= char <= 'я':
            new_string += chr((ord(char) - ord('а') + num_shift) % alphabet_length + ord('а'))
        else:
            new_string += char

    return new_string

print(cyrillic_shift(10))