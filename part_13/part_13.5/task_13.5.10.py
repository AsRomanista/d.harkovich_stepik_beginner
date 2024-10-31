# Напишите функцию convert_to_python_case(text),
# которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    snake_text = ''
    for i in text:
        if i.isupper():
            snake_text += ('_' + i)
        else:
            snake_text += i
    return snake_text[1:].lower()

txt = input()

print(convert_to_python_case(txt))
