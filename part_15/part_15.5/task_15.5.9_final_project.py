# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.
# Гарантируется, что между различными словами присутствует один пробел.

# delete special characters
def remove_special_char(text):
    specials = []
    cleaned_text = []

    for index, char in enumerate(text):
        if char.isalpha() or char.isspace():
            cleaned_text.append(char)
        else:
            specials.append((index, char))

    return ''.join(cleaned_text), specials

def restore_special_char(text, specials):
    text_list = list(text)

    for index, char in specials:
        if index not in range(len(text) + 1):
            text_list.insert(index, ' ')
        text_list.insert(index, char)


    return ''.join(text_list)

string = input()
text_without_specials, special_chars = remove_special_char(string)


def latin_shift(text):
    text_list = text.split()
    new_string_list = []

    for i in text_list:
        new_string = ''
        num_shift = len(i)

        for j in range(num_shift):
            if i[j].isalpha():
                if i[j].isupper():
                    if (ord(i[j]) + num_shift) <= ord('Z'):
                        new_string += chr(ord(i[j]) + num_shift)
                    else:
                        new_string += chr(ord(i[j]) + num_shift - 26)  # 26 - quantity of latin characters
                else:
                    if (ord(i[j]) + num_shift) <= ord('z'):
                        new_string += chr(ord(i[j]) + num_shift)
                    else:
                        new_string += chr(ord(i[j]) + num_shift - 26)  # 26 - quantity of latin characters
            else:
                new_string += i[j]

        new_string_list.append(new_string)

    return ' '.join(new_string_list)

shifted_text = latin_shift(text_without_specials)

final_text = restore_special_char(shifted_text, special_chars)
print(final_text)