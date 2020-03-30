import pickle, glob
for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>', record)

suefile = open('kab627.pkl', 'rb')
print(pickle.load(suefile)['brand']) # извлечь бренд записи kab627