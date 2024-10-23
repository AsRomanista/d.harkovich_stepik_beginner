# Напишите функцию convert_to_python_case(text),
# которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    snake_text = ''
    for i in range(len(text)):
        if text[i] == text[i].upper() and text[i].isalpha():
            snake_text += ('_' + text[i])
        else:
            snake_text += text[i]
    return snake_text[1:].lower()

txt = input()

print(convert_to_python_case(txt))
