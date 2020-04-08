import shelve
from all_class import Printers

fieldnames = ('brand', 'model', 'number', 'company')

db = shelve.open('class-shelve')
while True:
    key = input('\nKey? => ')
    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Printers(brand='?', model='?', number='?', company='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()