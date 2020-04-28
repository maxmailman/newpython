import sys

for f in (sys.stdin, sys.stdout, sys.stderr): print(f)

# <_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
# <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
# <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>

print('Hello!')
sys.stdout.write('Hello!' + '\n')

input('Say hello\n')
print('Say hello stdin\n'); sys.stdin.readline()[:-1]

