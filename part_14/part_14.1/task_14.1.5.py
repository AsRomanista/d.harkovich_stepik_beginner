# Интернет-магазин осуществляет экспресс доставку для своих товаров по цене 1000 рублей за первый товар и 120 рублей
# за каждый последующий товар. Напишите функцию get_shipping_cost(quantity),
# которая принимает в качестве аргумента натуральное число quantity – количество товаров в заказе –
# и возвращает стоимость доставки.

def get_shipping_cost(quantity):
    cost = 0
    for i in range(1, quantity + 1):
        if i == 1:
            cost = 1000
        elif i > 1:
            cost += 120
    return cost

n = int(input())

print(get_shipping_cost(n))