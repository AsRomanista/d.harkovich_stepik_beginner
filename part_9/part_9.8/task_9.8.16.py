# Все книги в домашней библиотеке Душнилы, друга Сэма, должны быть обязательно отсортированы по возрастанию:
# сначала по фамилиям авторов, а в случае совпадения фамилий – по названиям.
# Напишите программу, которая проверяет, верно ли отсортированы книги.
# На вход вашей программе поступает число n, а затем – n строк, каждая строка представляет собой книгу в следующем формате:
# <фамилия автора> <инициалы автора>, «<название книги>»
# Программа должна вывести «YES» (без кавычек), если книги отсортированы в соответствии с пожеланиями Душнилы,
# или «NO» (без кавычек) в противном случае.

# Примечание 1. Обратите внимание, что Душнила игнорирует инициалы автора при сортировке книг.
# Примечание 2. Гарантируется, что книги в наборе не повторяются.
# Примечание 3. Гарантируется, что фамилия автора состоит из одного слова.

# number = int(input())
#
# author = []
#
# for i in range(number):
#     author_book = input()
#     author_book = author_book.replace(author_book[(author_book.find(',') - 5):(author_book.find(','))], '') # delete initials
#     author.append(author_book)
#
# if author == sorted(author):
#     print('YES')
# else:
#     print('NO')

number = int(input())

book = input()
book = book.replace(book[(book.find(',') - 5):(book.find(','))], '')

for i in range(number - 1):
    book_next = input()
    book_next = book_next.replace(book_next[(book_next.find(',') - 5):(book_next.find(','))], '')
    if book > book_next:
        print('NO')
        break
    book = book_next
else:
    print('YES')



