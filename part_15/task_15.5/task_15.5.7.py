# Приведённый ниже текст был получен в результате шифрования алгоритмом Цезаря со сдвигом вправо на 25 символов:
# Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.
# Расшифруйте данный текст.

def encrypted_cyrillic_shift():
    num_shift = 7
    string = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
    new_string = ''

    for i in string:
        if i.isalpha():
            if i.isupper():
                if (ord(i) - num_shift) >= ord('А'):
                    new_string += chr(ord(i) - num_shift)
                else:
                    new_string += chr(ord(i) - num_shift + 32) # 32 - quantity of cyrillic characters without 'Ё'
            else:
                if (ord(i) - num_shift) >= ord('а'):
                    new_string += chr(ord(i) - num_shift)
                else:
                    new_string += chr(ord(i) - num_shift + 32) # 32 - quantity of cyrillic characters without 'Ё'
        else:
            new_string += i

    return new_string

print(encrypted_cyrillic_shift())