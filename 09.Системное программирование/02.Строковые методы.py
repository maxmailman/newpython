mystr = 'xxxSPAMxxx'
print('SPAM' in mystr)

print('Ni' in mystr)

print(mystr.find('Ni'))

mystr = '\t Ni \n'
print(mystr.strip()) # Удаляем пробельные символы
print(mystr.rstrip())
print(mystr.lstrip())

mystr = 'SHRUBBERY'
print(mystr.lower())  # shrubbery

print(mystr.isalpha())
print(mystr.isdigit())

mystr = 'aaaa,bbb,wer'
print(mystr.split(','))  # ['aaaa', 'bbb', 'wer']

mystr = 'a b\n c\nd'
print(mystr.split())  # ['a', 'b', 'c', 'd']

delim = 'NI'
print(delim.join(['aaaaa', 'dddd', 'dffdf']))  # aaaaaNIddddNIdffdf

print(' '.join(['A', 'dead', 'parot']))  # A dead parot

chars = list('Loreta')
print(chars)  # ['L', 'o', 'r', 'e', 't', 'a']

chars.append('!')
print(''.join(chars))  # Loreta!







