# На вход программе подается натуральное число n, затем n строк,
# затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы. Напишите программу,
# которая выводит все введенные строки, в которых встречаются одновременно все поисковые запросы.

number = int(input())

new_list = []

# all values in the list
for i in range(number):
    string = input()
    new_list.append(string)

search_number = int(input())
search_list = []

# all searching values in the list
for k in range(search_number):
    search_string = input().lower()
    search_list.append(search_string)

search_result = []

# check all strings
for j in range(len(new_list)):
    count = 0
    # check all search requests
    for search_string in search_list:
        if search_string in new_list[j].lower():
            count += 1
    # create search_result list
    if count == len(search_list):
        search_result.append(new_list[j])

print(*search_result, sep='\n')
