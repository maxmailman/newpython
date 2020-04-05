from initdata import kab625
import shelve

db = shelve.open('printers-shelve')

kab625 = db['kab625']
kab625['brand'] = 'samsung+'
db['kab625'] = kab625
db['kab000'] = kab625
db.close()