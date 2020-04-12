import shelve
from all_class import Printers, Second_printers

kab315 = Printers('keyocera', 2040, 4000)
kab625 = Second_printers('samsung', 4200, 54000)
kab626 = Second_printers(brand='Xerox', model='4342', number=300)

db = shelve.open('class-shelve')
db['kab315'] = kab315
db['kab625'] = kab625
db['kab626'] = kab626
db.close()