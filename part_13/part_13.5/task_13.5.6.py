# Напишите функцию is_one_away(word1, word2),
# которая принимает в качестве аргументов два слова word1 и word2 и возвращает значение True,
# если слова имеют одинаковую длину и отличаются ровно в одном символе,
# или значение False в противном случае.

def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count_dif = 0
    for i in range(len(word1)):
        if word1[i] not in word2[i]:
            count_dif += 1
    if count_dif == 1:
        return True
    else:
        return False

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))



