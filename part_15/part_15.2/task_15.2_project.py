# Подключите модуль random;
# Сгенерируйте случайное число от 1 до 100
# Выведите текст приветствия пользователю: 'Добро пожаловать в числовую угадайку'.

import random

right_border = input('Enter maximum number: ')

while True:
    if right_border.isdigit() and int(right_border) > 1:
        break
    else:
        print('Enter a number greater than one')

random_number = random.randint(1, int(right_border))
print('Welcome to the number guessing game')

# Функция проверки корректности введенных данных
# Пользователь потенциально может ввести неверные данные, например, не число, или число превышающее 100.
# Важно предусмотреть такую возможность, чтобы программа продолжала правильно работать.
# Обработка такого рода ситуаций называется защитой от дурака.
# Напишите функцию is_valid() в которую передается один строковый аргумент.
# Функция возвращает значение True если переданный аргумент является целым числом от 1 до 100
# и False в противном случае.

def is_valid(random_number):
    if 1 <= int(random_number) <= int(right_border) and random_number.isdigit():
        return True
    else:
        return False

# Организуйте цикл, который будет запрашивать у пользователя данные
# (цикл может быть бесконечным (while True) или может использовать сигнальную метку с последующим переключением,
# после угадывания числа);
# Запросите у пользователя число от 1 до 100
# Проверьте введенные данные с помощью функции is_valid():
# если данные некорректны, выведите текст: 'А может быть все-таки введем целое число от 1 до 100?'
# и перейдите к следующей итерации основного цикла;
# если данные корректны, преобразуйте их к целому числу для удобства дальнейшей работы.

again = 'y'

while again.lower() == 'y':
    attempts = 0
    while True:
        guess_number = input(f'Enter any number from 1 to {right_border} inclusive: ')
        attempts += 1
        if not is_valid(guess_number):
            print(f'Maybe we should enter an integer between 1 and {right_border}?')
        else:
            if int(guess_number) < random_number:
                print('Your number is less than the guessed one, try again')
            elif int(guess_number) > random_number:
                print('Your number is higher than the guessed one, try again')
            else:
                print('You guessed it, congratulations!')
                print(f'Number of attempts: {attempts}')
                again = input('Do you want to play again? (y = yes, n = no): ')
                break

print('Thanks for playing the number guessing game. See you later...')

# Добавьте подсчет попыток, сделанных пользователем. Когда число отгадано, программа должна показать количество попыток; - done
# Добавьте возможность генерации нового числа (повторная игра), после того, как пользователь угадал число; - done
# Добавить возможность указания правой границы для случайного выбора числа (от 1 до n). - done

