# Напишите программу, выводящую следующий список:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

alphabet_list = []
counter = 1

for i in range(97, 123):
    alphabet_list.append(chr(i) * counter)
    counter += 1

print(alphabet_list)