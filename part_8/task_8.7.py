# Напишите программу, которая находит аналогичные интересные числа (сумма двух кубов разными способами).
# В ответе запишите первые 5 чисел в порядке возрастания, включая число 1729

total = 0

for x in range(33):
    for y in range(x + 1, 33):
        for z in range(x + 1, 33):
            for k in range(z + 1, 33):
                if (x**3 + y**3) == (z**3 + k**3):
                    total += 1
                    s = (x ** 3 + y ** 3)
                    print(s, x, y, z, k)
    if total == 5:
        break



