from initdata import kab315, kab625, kab626, kab627
import pickle
for (key, record) in [('kab315', kab315), ('kab625', kab625), ('kab626', kab626), ('kab627', kab627)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()