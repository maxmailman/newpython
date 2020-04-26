import subprocess
import os

print(subprocess.call('python os_path.py'))

print(subprocess.call('cmd /C "type os_path.py"'))

print(subprocess.call('type os_path.py', shell=True))

# os.startfile('test.docx')

# Особенности итерации в os.popen
I = os.popen('dir /B *.py')
I = iter(I)
I.__next__()
print(next(I))
print(next(I))
print(next(I))


