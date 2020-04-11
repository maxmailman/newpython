import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key].brand, db[key].model, db[key].company, db[key].number)

kab626 = db['kab626']
kab626.add_number(2)
db['kab626'] = kab626
for key in db:
    print(key, '=>\n', db[key].brand, db[key].model, db[key].company, db[key].number)
db.close()