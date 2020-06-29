import numpy

n,m = map(int,input().split())

numpy.set_printoptions(legacy = '1.13')
arr = numpy.array([input().split() for i in range (n) ], int)

print (numpy.mean(arr, axis =1))
print (numpy.var(arr, axis =0))
print (numpy.std(arr, axis =None))