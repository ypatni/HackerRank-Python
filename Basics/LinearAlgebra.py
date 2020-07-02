import numpy

n= int(input())
numpy.set_printoptions(legacy='1.13')
arr = numpy.array([input().split() for i in range (n) ], float)
print (numpy.linalg.det(arr)) 