# Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке.
# Проблема заключается в том, что данный метод не находит местоположение всех символов а.
# Напишите функцию с именем find_all(target, symbol),
# которая принимает два аргумента: строку target и символ symbol и возвращает список,
# содержащий все местоположения этого символа в строке.

def find_all(target, symbol):
    result = [target_number for target_number in range(len(target)) if target[target_number] == symbol]
    return result

s = input()
char = input()

print(find_all(s, char))