money = int(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9,'ВТБ': 4.28, 'СБЕР': 4.0}
total = [x * money / 100 for x in list(per_cent.values())]
deposit = list(map(round, total))
print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать-", max(deposit))
