# Модератору Сэму за каждый символ его сообщений в комментариях Тимур платит в 🐝 (пчелках-coin) по следующему тарифу:
# <код символа в таблице Unicode>×3🐝
# А стоимость всего сообщения складывается из суммы стоимостей всех символов.
# Сэму захотелось подсчитать, сколько 🐝 он зарабатывает за свои ответы в комментариях, и просит вас помочь ему.
# На вход программе подается строка текста.
# Требуется написать программу, которая находит стоимость сообщения Сэма в 🐝 и выводит текст в следующем формате:
# Текст сообщения: '<текст сообщения Сэма>'
# Стоимость сообщения: <стоимость сообщения Сэма>🐝

string = input()

total = 0

for i in string:
    total += ord(i)

total = total * 3

print(f"Message text: '{string}'", f'Cost of message: {total}🐝', sep='\n')