# На вход программе подаётся одна строка с буквами русского языка.
# Напишите программу, которая определяет количество гласных и согласных букв и выводит текст в следующем формате:
# Количество гласных букв равно <кол-во гласных букв>
# Количество согласных букв равно <кол-во согласных букв>

string = input()

vowels = 'аеиоуыэюяАЕИОУЫЭЮЯ'
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
total_vowels = 0
total_consonants = 0

for i in range(len(string)):
    if string[i] in vowels:
        total_vowels += 1
    elif string[i] in consonants: # no need to check the first conditions again
        total_consonants += 1

print('The number of vowels is equal to', total_vowels)
print('The number of consonants is equal to', total_consonants)
