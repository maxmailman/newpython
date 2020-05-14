file = open('data.txt')
lines = file.readlines()
for line in lines:
    print(line, end='')

file.seek(0) # Переходим в начало файла
print(file.readlines()) # Читаем файл заново целиком

file.seek(0) # Переходим в начало файла
print(file.readline()) # Читаем первую строку

print(file.readline())
print(file.readline()) # Конец файла - пустая строка

for line in open('data2.txt'):
    print(line, end='')






