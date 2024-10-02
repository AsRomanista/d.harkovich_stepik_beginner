# Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали и любезно соглашается помочь им
# в решении их проблем.
# Одной из такой проблем являлся странный компьютерный вирус, который проявлялся в виде появления комментариев к программам
# на терминалах Братства Стали.
# Известно, что программисты Братства никогда не оставляют комментарии к коду и пишут программы на Python,
# поэтому удаление всех этих комментариев никак не навредит им. Помогите писцу Ибсену удалить все комментарии из программы.

number = input()

number_list = []

for _ in number:
    if _ != '#':
        number_list.append(_)

number_list_new = int(''.join(number_list))


all_right_string_list = []

for i in range(number_list_new):
    string = input()
    right_string = ''
    for j in string:
        if j != '#':
            right_string += j
        else:
            break

    if right_string.strip():
        all_right_string_list.append(right_string.rstrip())


for string1 in all_right_string_list:
    print(string1)