kab626 = [['brand', 'keyocera'], ['model', 2040], ['number', 35000]]
kab627 = [['brand', 'xerox'], ['model', 1030], ['number', 10000]]
kab625 = [['brand', 'samsung'], ['model', 42000], ['number', 54000]]

printers = [kab627, kab626, kab625]

for pr in printers:
    print(pr[0][1], pr[1][1])

print([models[1][1] for models in printers])

# Просматривать имена полей в цикле, отыскивая необходимые (в следующем цикле используется
# операция присваивания кортежа для распаковывания пар имя/значение)
for num in printers:
    for (name, value) in num:
        if name == 'number':
            print(value)


# for num in printers:
#     print(num)

# Попробуем функцию
def trx(prnt, value):
    for (fname, fvalue) in prnt:
        if fname == value:
            return fvalue

# print(trx(kab625, 'number'))

for rec in printers:
    print(trx(rec, 'model'))


# # Цикл переделаный в функцию
# def trx2(prnt, value):
#     for num in prnt:
#         for (fname, fvalue) in num:
#             if fname == value:
#                 print(fvalue)
#
#
# trx2(printers, 'brand')
