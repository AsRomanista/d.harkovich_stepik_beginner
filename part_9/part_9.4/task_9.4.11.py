# На вход программе подается строка текста.
# Напишите программу, которая подсчитывает количество цифр в данной строке.

string = input()
numbers = '0123456789'
total = 0

for i in range(len(string)):
    if string[i] in numbers:
        total += 1
print(total)

# more interesting decision

text = input()
cnt = 0

for i in range(10):
    cnt += text.count(str(i))

print(cnt)