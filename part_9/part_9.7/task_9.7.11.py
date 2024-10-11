# Как вы помните из прошлой задачи, модератору Сэму за каждый символ его сообщений в комментариях 
# Тимур платит в 🐝 (пчелках-coin) по следующему тарифу:
# <код символа в таблице Unicode>×3🐝
# А стоимость всего сообщения складывается из суммы стоимостей всех символов. 
# На этот раз Сэму захотелось схитрить и попробовать увеличить стоимость своего сообщения, 
# заменив в нем некоторые английские буквы на русские. 
# Как вы помните, русские буквы в таблице Unicode находятся после английских.
# Сэм хочет заменить следующие английские буквы: eyopaxcETOPAHXCBM
# на соответствующие им русские буквы: еуорахсЕТОРАНХСВМ
# Тимур визуально разницу не заметит, а Сэм сможет зарабатывать больше пчелок-coin. 😊
# На вход программе подается строка текста. 
# Требуется написать программу, которая находит стоимость старого и нового сообщений 
# Сэма в 🐝 и выводит текст в следующем формате:
# Старая стоимость: <стоимость старого сообщения>🐝
# Новая стоимость: <стоимость нового сообщения>🐝

string = input()

cyrrilic = 'еуорахсЕТОРАНХСВМ'
latin = 'eyopaxcETOPAHXCBM'

total_old = 0
total_new = 0

for i in string:
    total_old += ord(i)
    if i in latin:
        i = cyrrilic[latin.find(i)]
    total_new += ord(i)

total_old *= 3
total_new *= 3

print(f'Old price: {total_old}🐝')
print(f'New price: {total_new}🐝')