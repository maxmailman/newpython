kab625 = {'brand': 'samsung', 'model': 42000, 'number': 54000}
kab626 = {'brand': 'keyocera', 'model': 2040, 'number': 35000}
kab627 = {'brand': 'xerox', 'model': 1030, 'number': 10000}
kab315 = dict(brand='keyocera', model=2040, number=4000) # Быстрое создание словаря

print(kab625['model'])
print(kab315)

printers = [kab315, kab625, kab626, kab627]

for rec in printers:
    print(rec['brand'], rec['model'])

for rec in printers:
    if rec['brand'] == 'keyocera':
        print(rec)

brands = [br['brand'] for br in printers]
print(brands)

print(list(map((lambda x: x['brand']), printers))) # То же самое

print(sum(num['number'] for num in printers)) # Сумма страниц