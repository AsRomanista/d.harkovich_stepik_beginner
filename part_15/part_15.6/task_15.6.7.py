# Переведите десятичное число 1000 в шестнадцатеричную систему счисления.


number, result = int(input()), ''

while number > 0:
    if number % 16 >= 10:
        result += chr(65 + (number % 16) % 10)
    else:
        result += str(number % 16)
    number //= 16
print(result[::-1])


