from itertools import product

a = map(int, input().split())
b = map(int, input().split())

for x in product(a,b):
    print (x, end=' ')