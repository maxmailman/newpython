import pickle
dbfile = open('printers-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>', db[key])
print(db['kab315'])
