# Подключите модуль random;
# Создайте список answers, содержащий 20 потенциальных ответов (Бесспорно, Предрешено, и т.д.).

import random

replies = [
    "Undoubtedly",
    "It's predetermined",
    "No doubts about it",
    "Definitely yes",
    "You can be sure of that",
    "I think so - yes",
    "Most likely",
    "Good prospects",
    "The signs say - yes",
    "Yes",
    "Unclear at the moment, try again later",
    "Ask later",
    "Better not to say",
    "Cannot predict right now",
    "Concentrate and ask again",
    "According to my data - no",
    "Highly doubtful",
    "The prospects are not very good",
    "My answer is no",
    "Don't even think about it",
]

# Выведите текстовое сообщение: 'Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.';
# Уточните как зовут пользователя;
# Выведите слова приветствия, например, 'Привет Тимур'.

print('Hello World, I am a magic ball and I know the answer to any question you have.')
name = input('What is your name? ')
print(f'Hello, {name}')

# Организуйте цикл, который будет запрашивать у пользователя данные;
# Запросите у пользователя вопрос;
# Выведите случайный ответ с помощью функции choice() передав список answers в качестве аргумента;
# Уточните у пользователя, хочет ли он задать еще один вопрос, если да, то вернитесь в основной цикл программы,
# если нет выведите сообщение 'Возвращайся если возникнут вопросы!' и завершите программу.


def choice():
    return random.choice(replies)

again = 'y'

while again.lower() == 'y':
    question = input('What do you want to ask the magic cube? ')
    print(choice())
    again = input('Do you want to ask another question? (y = yes, n = no): ')

print('Come back if you have any questions!')





