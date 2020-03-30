kab315 = dict(brand='keyocera', model=2040, number=4000)
kab625 = dict(brand='samsung', model=4200, number=54000)
kab626 = dict(brand='xerox', model=1030, number=10000)
kab627 = dict(brand='keyocera', model=2540, number=15000)

print(kab627)

db = {}

db['kab315'] = kab315
db['kab625'] = kab625

print(db)
print(db['kab315']['brand'])

import pprint  # Модуль форматированного вывода БД

pprint.pprint(db)

for key in db:
    print(key, '=>', db[key]['brand'])

for key in db:
    print(key, '=>', db[key]['model'])

print(db.values())

x = [db[key]['brand'] for key in db]
print(x)

x = [rec['brand'] for rec in db.values()]
print(x)

db['kab314'] = dict(brand='hp', model=4515, number=85669)
db['kab626'] = dict(brand='xerox', model=1030, number=1000)
db['kab627'] = dict(brand='keyocera', model=2540, number=15000)
pprint.pprint(db)

print(list(db.keys()))
print(len(db))

print([rec['model'] for rec in db.values() if rec['brand'] == 'keyocera'])  # SQL подобный запрос

print([rec['model'] for rec in db.values() if 4000 < rec['number'] < 80000]) # SQL подобный запрос








