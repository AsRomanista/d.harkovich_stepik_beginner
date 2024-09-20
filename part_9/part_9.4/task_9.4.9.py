# На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин).
# Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.

string = input()
lower_case = string.lower()

print('Adenine:', lower_case.count('а'))
print('Guanine:', lower_case.count('г'))
print('Cytosine:', lower_case.count('ц'))
print('Timin:', lower_case.count('т'))