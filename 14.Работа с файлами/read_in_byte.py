print(open('data.txt').read())
print(open('data.txt', 'rb').read())

file = open('data.txt', 'rb')
for line in file: print(line)

open('data3.bin', 'wb').write(b'Spamm!\n')
print(open('data3.bin', 'rb').read())
#open('data3.bin', 'wb').write('Spamm!')
