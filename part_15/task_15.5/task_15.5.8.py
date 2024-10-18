# Приведённый ниже текст был получен в результате шифрования алгоритмом Цезаря со сдвигом вправо на n символов:
# Hawnj pk swhg xabkna ukq nqj.
# Расшифруйте данный текст.

string = 'Hawnj pk swhg xabkna ukq nqj.'

def encrypted_latin_shift(string, num_shift):
    new_string = ''

    for i in string:
        if i.isalpha():
            if i.isupper():
                if (ord(i) - num_shift) >= ord('A'):
                    new_string += chr(ord(i) - num_shift)
                else:
                    new_string += chr(ord(i) - num_shift + 26) # 26 - quantity of latin characters
            else:
                if (ord(i) - num_shift) >= ord('a'):
                    new_string += chr(ord(i) - num_shift)
                else:
                    new_string += chr(ord(i) - num_shift + 26) # 26 - quantity of latin characters
        else:
            new_string += i

    return new_string

for num_shift in range(1, 26):
    print(f'num_shift = {num_shift}: {encrypted_latin_shift(string, num_shift)}')

