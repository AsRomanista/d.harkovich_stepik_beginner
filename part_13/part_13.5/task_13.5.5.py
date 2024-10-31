# Напишите функцию is_password_good(password),
# которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True,
# если пароль является надежным и False - в противном случае.
# Пароль является надежным если:
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

def is_password_good(password):
    return len(password) >= 8 \
        and any(c.isdigit() for c in password) \
        and any(c.islower() for c in password) \
        and any(c.isupper() for c in password)

txt = input()

print(is_password_good(txt))