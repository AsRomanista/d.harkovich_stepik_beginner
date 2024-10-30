# На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел. Напишите программу,
# которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(),
# а затем выводит его.


# code from 13.4.10
def quick_merge(list1, list2):
    result = []

    p1 = 0  # pointer to the first element of the list list1
    p2 = 0  # pointer to the first element of list2

    while p1 < len(list1) and p2 < len(list2):  # so far none of the lists have been completed
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    result += list1[p1:] if p1 < len(list1) else list2[p2:]
    return result

# -----------------------

string_number = int(input())

lists = [int(num) for num in input().split()]


for _ in range(string_number - 1):
    current_list = [int(num) for num in input().split()]
    lists = quick_merge(lists, current_list)

print(*lists)