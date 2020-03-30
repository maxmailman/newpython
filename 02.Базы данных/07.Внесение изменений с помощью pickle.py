import pickle
dbfile = open('printers-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['kab627']['number'] = 10000

dbfile = open('printers-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()