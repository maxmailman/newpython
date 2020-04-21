file = open('spam', 'w')
file.write(('spam'*5) + '\n')
file.close()

file = open('spam')
text = file.read()
print(text)
