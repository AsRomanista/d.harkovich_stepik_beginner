# На вход программе подаются 3 различных слова.
# Вам необходимо отсортировать эти слова по возрастанию в лексикографическом порядке
# и вывести их на одной строке, разделяя символом пробела.

word1, word2, word3 = input(), input(), input()

max_word = max(word1, word2, word3)
min_word = min(word1, word2, word3)

total = word1 + word2 + word3
delete_min = total.replace(min_word, '')
delete_max = delete_min.replace(max_word,'')

print(min_word, delete_max, max_word)