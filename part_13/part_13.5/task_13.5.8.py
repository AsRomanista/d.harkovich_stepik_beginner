# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True,
# если пароль является действительным паролем BEEGEEK банка, или False в противном случае.

def is_palindrome(text):
    no_spec = [symbols.lower() for symbols in text if symbols.isalpha() or symbols.isdigit()]
    if no_spec == no_spec[::-1]:
        return True
    else:
        return False

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_valid_password(password):
    list_password = password.split(':')
    if len(list_password) == 3:
        if is_palindrome(list_password[0]) and is_prime(int(list_password[1])) and is_even(int(list_password[2])):
            return True
        else:
            return False
    else:
        return False

psw = input()

print(is_valid_password(psw))

