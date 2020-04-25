import os

print(os.getpid())
print(os.getcwd())
os.chdir(r'C:\Users')
print(os.getcwd())


print(os.path.isdir(r'C:\Users'))   # True
print(os.path.isfile(r'C:\Users'))  # False

print(os.path.abspath('')) # Реальный рабочий каталог в данный момент

print(os.popen('dir /B').readlines()) # ['Max\n', 'Public\n', 'User\n']



