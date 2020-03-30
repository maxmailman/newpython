# Записи
kab315 = dict(brand='keyocera', model=2040, number=4000)
kab625 = dict(brand='samsung', model=4200, number=54000)
kab626 = dict(brand='xerox', model=1030, number=10000)
kab627 = dict(brand='keyocera', model=2540, number=15000)

# База данных
db = {}
db['kab315'] = kab315
db['kab625'] = kab625
db['kab626'] = kab626
db['kab627'] = kab627

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n', db[key])

