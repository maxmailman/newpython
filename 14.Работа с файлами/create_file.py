file = open('data.txt', 'w')
file.write('Hello file data!\n')
file.write('Bye file data.\n')
file.close()
#
file = open('data2.txt', 'w')
file.writelines(['Hello!\n', 'Bye!\n'])
file.close()

#Можно не использовать метод close. Приведем пример чтения временного файлв
open('some_data.txt', 'w').write('Hello Max!\n')
print(open('some_data.txt', 'r').read())




