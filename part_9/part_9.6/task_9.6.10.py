# Очень часто студенты "Поколения Python" путают понятия «сумма кубов» и «куб суммы».
# Для того чтобы внести ясность в этот извечный математический вопрос, предлагаем вам решить следующую задачу.
# На вход программе подаются два целых числа a и b.
# Ваша программа должна посчитать для этих чисел сумму их кубов и куб их суммы и вывести результат вычислений в следующем формате:
# Для чисел <число a> и <число b>:
#   Сумма кубов: <число a>**3 + <число b>**3 = <сумма кубов a и b>
#   Куб суммы: (<число a> + <число b>)**3 = <куб суммы a и b>

a = int(input())
b = int(input())
sum_cubes = a**3 + b**3
cube_sum = (a + b)**3

print(f'For numbers {a} and {b}:')
print(f'  Sum of cubes: {a}**3 + {b}**3 = {sum_cubes}')
print(f'  Cube of the sum: ({a} + {b})**3 = {cube_sum}')