# Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел-палиндромов от [100:1000]

palindromes = [int(digit) for digit in range(100, 1001) if str(digit)[0] == str(digit)[-1]]

print(palindromes)