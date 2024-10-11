# Используя метод format(), дополните приведённый код так, чтобы он вывел текст:
# In 2010, someone paid 10k Bitcoin for two pizzas.

year = 2010
value = '10k'
thing = 'Bitcoin'

s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, value, thing)

print(s)