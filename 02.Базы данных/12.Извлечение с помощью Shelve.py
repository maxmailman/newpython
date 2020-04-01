import shelve

db = shelve.open('printers-shelve')
for key in db:
    print(key, '=>', db[key])

print(db['kab625']['brand'])
db.close()