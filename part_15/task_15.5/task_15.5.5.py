# Зашифруйте приведённый ниже текст алгоритмом Цезаря со сдвигом вправо на 10 символов:
# Блажен, кто верует, тепло ему на свете!
# Примечание. Считайте, что русский алфавит состоит из 32 букв (буква ё отсутствует).

def cyrillic_shift():
    num_shift = 10
    string = 'Блажен, кто верует, тепло ему на свете!'
    new_string = ''

    for i in string:
        if i.isalpha():
            if i.isupper():
                if (ord(i) + num_shift) <= ord('Я'):
                    new_string += chr(ord(i) + num_shift)
                else:
                    new_string += chr(ord(i) + num_shift - 32) # 32 - quantity of cyrillic characters without 'Ё'
            else:
                if (ord(i) + num_shift) <= ord('я'):
                    new_string += chr(ord(i) + num_shift)
                else:
                    new_string += chr(ord(i) + num_shift - 32) # 32 - quantity of cyrillic characters without 'Ё'
        else:
            new_string += i

    return new_string

print(cyrillic_shift())