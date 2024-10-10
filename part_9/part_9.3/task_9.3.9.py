# На вход программе подается строка.
# Напишите программу, которая меняет регистр символов, другими словами замените все строчные символы заглавными и наоборот.

string = input()

print(string.swapcase())

# via 'for'
new_string = ''

for i in string:
    if i.islower() and i.isalpha():
        new_string += i.upper()
    elif i.isupper() and i.isalpha():
        new_string += i.lower()
    else:
        new_string += i

print(new_string)