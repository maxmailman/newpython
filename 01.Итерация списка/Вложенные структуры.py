kab625 = {'name': {'brans':'samsung', 'model': 42000},
          'number': 54000,
          'users': ['us1', 'us2', 'us3'],
          'year': (2015, 2016, 2017, 2018, 2019, 2020)}

# kab626 = {'brand': 'keyocera', 'model': 2040, 'number': 35000}
# kab627 = {'brand': 'xerox', 'model': 1030, 'number': 10000}

print(kab625['name'])
print(kab625['name']['model'])
print(kab625['year'][2])

kab625['users'].append('us4')
print(kab625['users'])

for us in kab625['year']:
    print(us)

