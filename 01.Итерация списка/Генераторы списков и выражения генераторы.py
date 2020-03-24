kab626 = ['keyocera', 2040, 35000]
kab627 = ['xerox', 1030, 10000]
kab625 = ['samsung', 4200, 54000]

printers = [kab625, kab626, kab627]

for p in printers:
    print(p)

pts = [pr[1] for pr in printers] # Создание нового списка выборкой из другого (старый способ)
print(pts)

sel = [rt[2] for rt in printers] # Создание нового списка выборкой из другого (старый способ)
print(sel)

sel = map((lambda x: x[2]), printers) # Создание списков в версиях 3.X , функция map вызывает генератор
print(list(sel))

sum = sum(s[2] for s in printers) # выражение генератор, sum - встроенная функция
print(sum)

# Для добавления новых записей в базу данных вполне достаточно использовать
# обычные операции над списками, такие как append и extend
printers.append(['brother', 0, 0])
print(printers[-1])
print(printers[-1][0])





