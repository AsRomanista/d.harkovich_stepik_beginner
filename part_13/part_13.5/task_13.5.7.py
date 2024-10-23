# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text
# и возвращает значение True если указанный текст является палиндромом
# и False в противном случае.

def is_palindrome(text):
    no_spec = [symbols.lower() for symbols in text if symbols.isalpha() or symbols.isdigit()]
    return no_spec == no_spec[::-1]

txt = input()

print(is_palindrome(txt))

