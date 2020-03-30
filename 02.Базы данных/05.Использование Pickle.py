# Данный скрипт сохраняет все в файл благодаря импортируемому модулю pikcke
from initdata import db
import pickle
dbfile = open('printers-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()

#