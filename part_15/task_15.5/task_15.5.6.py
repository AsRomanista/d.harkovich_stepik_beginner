# Зашифруйте приведённый ниже текст алгоритмом Цезаря со сдвигом вправо на 17 символов:
# To be, or not to be, that is the question!

def latin_shift():
    num_shift = 17
    string = 'To be, or not to be, that is the question!'
    new_string = ''

    for i in string:
        if i.isalpha():
            if i.isupper():
                if (ord(i) + num_shift) <= ord('Z'):
                    new_string += chr(ord(i) + num_shift)
                else:
                    new_string += chr(ord(i) + num_shift - 26) # 26 - quantity of latin characters
            else:
                if (ord(i) + num_shift) <= ord('z'):
                    new_string += chr(ord(i) + num_shift)
                else:
                    new_string += chr(ord(i) + num_shift - 26) # 26 - quantity of latin characters
        else:
            new_string += i

    return new_string

print(latin_shift())