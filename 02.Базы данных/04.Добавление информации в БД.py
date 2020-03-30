from make_db_file import loadDbase, storeDbase
db = loadDbase()
db['kab315']['number']=5000
storeDbase(db)

