# Напишите функцию is_password_good(password),
# которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True,
# если пароль является надежным и False - в противном случае.
# Пароль является надежным если:
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

def is_password_good(password):
    if len(password) < 8:
        return False

    upper_case = False
    lower_case = False
    number = False

    for i in password:
        if i.isupper():
            upper_case = True
        elif i.islower():
            lower_case = True
        elif i.isdigit():
            number = True
    return upper_case and lower_case and number


txt = input()

print(is_password_good(txt))