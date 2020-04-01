from initdata import kab315, kab625, kab626, kab627
import shelve
db = shelve.open('printers-shelve')
db['kab351'] = kab315
db['kab625'] = kab625
db.close()
