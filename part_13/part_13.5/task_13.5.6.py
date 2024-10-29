# Напишите функцию is_one_away(word1, word2),
# которая принимает в качестве аргументов два слова word1 и word2 и возвращает значение True,
# если слова имеют одинаковую длину и отличаются ровно в одном символе,
# или значение False в противном случае.

def is_one_away(word1, word2):
    count_dif = 0
    if len(word1) != len(word2):
        return False
    else:
        return sum(1 for i in range(len(word1)) if word1[i] != word2[i]) == 1

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))


