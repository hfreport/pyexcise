import os

vec = [1,3,5,7,9]

for x in vec:
    print(x)

v = [[x, 2*x] for x in vec]

print(v)

print(os.system('ifconfig'))
