# На вход программе подается одна строка.
# Напишите программу, которая определяет сколько в ней одинаковых соседних символов.

string = input()
total = 0

for i in range(0, len(string) - 1):
    if string[i] == string[i + 1]:
        total += 1
print(total)
