import shelve

fieldnames = ('brand', 'model', 'number', 'company')
print(fieldnames)
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')

    if not key: break
    try:
        record = db[key]  # Извлечь запись по ключу и вывести
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))

db.close()