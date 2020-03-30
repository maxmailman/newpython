import pickle
kabfile = open('kab315.pkl', 'rb')
kab = pickle.load(kabfile)
kabfile.close()
kab['number'] = 10000
kabfile = open('kab315.pkl', 'wb')
pickle.dump(kab, kabfile)
kabfile.close()