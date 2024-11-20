# Приведённый ниже текст был получен в результате шифрования алгоритмом Цезаря со сдвигом вправо на 25 символов:
# Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.
# Расшифруйте данный текст.

def encrypted_cyrillic_shift():
    num_shift = 7
    text = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
    new_string = ''
    alphabet_length = 32

    # for i in text:
    #     if i.isalpha():
    #         if i.isupper():
    #             if (ord(i) - num_shift) >= ord('А'):
    #                 new_string += chr(ord(i) - num_shift)
    #             else:
    #                 new_string += chr(ord(i) - num_shift + 32) # 32 - quantity of cyrillic characters without 'Ё'
    #         else:
    #             if (ord(i) - num_shift) >= ord('а'):
    #                 new_string += chr(ord(i) - num_shift)
    #             else:
    #                 new_string += chr(ord(i) - num_shift + 32) # 32 - quantity of cyrillic characters without 'Ё'
    #     else:
    #         new_string += i

    # return new_string

    for char in text:
        if 'А' <= char <= 'Я':
            new_string += chr((ord(char) - ord('А') - num_shift) % alphabet_length + ord('А'))
        elif 'а' <= char <= 'я':
            new_string += chr((ord(char) - ord('а') - num_shift) % alphabet_length + ord('а'))
        else:
            new_string += char

    return new_string

print(encrypted_cyrillic_shift())