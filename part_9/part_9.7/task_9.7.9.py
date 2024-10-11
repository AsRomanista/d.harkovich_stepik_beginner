# Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова.
# Напишите программу, которая принимает 4 слова и находит среди них самое тяжелое слово.
# Если самых тяжелых слов будет несколько, то программа должна вывести первое из них.

weight = 0
max_word = ''

for i in range(4):
    word = input()
    total = 0
    for j in word:
        total += ord(j)
    if total > weight:
        weight = total
        max_word = word

print(max_word)


