import sys
import os

print(sys.argv)

print(os.environ.keys())

print(list(os.environ.keys()))
print('\n')
print(os.environ['COMPUTERNAME'])
print(os.environ['TEMP'])

print(os.pathsep)
print(os.environ['PYTHONPATH'])
for i in os.environ['PYTHONPATH'].split(os.pathsep):
    print(i)
