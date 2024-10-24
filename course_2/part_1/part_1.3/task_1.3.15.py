# Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
# Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
# Ваша программа должна вывести единственное число: C(n, k).

n, k = map(int, input().split())

def combination(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return combination(n - 1, k) + combination(n - 1, k - 1)

print(combination(n, k))
