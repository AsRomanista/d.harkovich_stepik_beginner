# Подключите модуль random;
# Создайте глобальный список word_list, содержащий слова, которые будут использоваться в игре.

import random

WORD_LIST = ['Hello', 'world']

# Напишите функцию get_word() которая возвращает случайное слово из списка word_list в верхнем регистре.

def get_word():
    return random.choice(WORD_LIST).upper()

stages = [  # final state: head, torso, both arms, both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, torso, both arms, one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, torso, both arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, torso and one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # initial state
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]

def display_hangman(tries):
    return stages[tries]

# Напишите функцию play(), в которой будет осуществляться основная логика игры.
# Функция play() принимает в качестве аргумента слово word, сгенерированное функцией  get_word()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Let\'s play word guessing game!')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input('Enter a letter or a whole word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already named the letter', guess)
            elif guess not in word:
                print('This letter', guess, 'isn\'t in the word')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Great job, letter', guess, 'is in the word')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indexes = [i for i in range(len(word)) if word[i] == guess]
                for letter in indexes:
                    word_as_list[letter] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already said the word', guess)
            elif guess != word:
                print('Word', guess, 'is not true.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Enter a letter or word.')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Congratulations, you guessed the word! You won!')
    else:
        print('You didn\'t guess the word. The word you were trying to guess was ' + word)

again = 'y'

while again.lower() == 'y':
    word = get_word()
    play(word)
    again = input('Let\'s play again? (y = yes, n = no):')



