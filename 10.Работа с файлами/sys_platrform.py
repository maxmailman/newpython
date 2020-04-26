import sys
print(sys.platform, sys.maxsize, sys.version)

if sys.platform[:3] == "win": print('hello windows')

print(sys.path)

