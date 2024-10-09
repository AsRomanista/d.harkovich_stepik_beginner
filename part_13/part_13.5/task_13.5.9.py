# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
# состоящую из символов ( и ) и возвращает значение True,
# если поступившая на вход строка является правильной скобочной последовательностью,
# или значение False в противном случае.

def is_correct_bracket(text):
    count = 0
    for i in range(len(text)):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
            if count < 0:
                return False
    if count != 0:
        return False
    else:
        return True

txt = input()

print(is_correct_bracket(txt))
