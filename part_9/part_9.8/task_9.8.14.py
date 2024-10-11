# На вход программе подаются 2 строки. Вам необходимо сравнить эти строки посимвольно,
# не учитывая регистр и игнорируя все небуквенные символы.
# Программа должна вывести «YES», если строки окажутся равны в результате такой проверки, или «NO» в противном случае.

first_string = input()
second_string = input()

new_first_string = ''
new_second_string = ''

for i in first_string:
    if i.isalpha():
        new_first_string += i

for i in second_string:
    if i.isalpha():
        new_second_string += i

if new_first_string.lower() == new_second_string.lower():
    print('YES')
else:
    print('NO')
