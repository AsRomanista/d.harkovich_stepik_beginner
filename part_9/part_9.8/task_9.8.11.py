# На вход программе подается последовательность строк, каждая строка на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» (без кавычек).
# При этом само слово «КОНЕЦ» не входит в последовательность, лишь символизируя ее окончание.
# Напишите программу, которая находит в данной последовательности максимальную и минимальную строки
# (в лексикографическом порядке) и выводит их в следующем формате:
# Минимальная строка ⬇️: <минимальная строка>
# Максимальная строка ⬆️: <максимальная строка>

# all_string = []
#
# while True:
#     string = input()
#     if string == 'THE END':
#         break
#     all_string.append(string)
#
# if all_string:
#     min_string = min(all_string)
#     max_string = max(all_string)
#     print(f'Minimum line ⬇️: {min_string}')
#     print(f'Max line ⬆️: {max_string}')

string = input()

max_string = string
min_string = string

while string != 'THE END':
    if string < min_string:
        min_string = string
    if string > max_string:
        max_string = string

    string = input()


print(f'Minimum line ⬇️: {min_string}')
print(f'Max line ⬆️: {max_string}')

