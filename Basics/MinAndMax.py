import numpy

n,m = map(int,input().split())

    
arr = numpy.array([input().split() for i in range (n) ], int)

print (numpy.max(numpy.min(arr, axis =1), axis = 0))
