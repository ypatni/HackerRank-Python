import numpy

n= int(input())

    
arr = numpy.array([input().split() for i in range (n) ], int)
arr2 = numpy.array([input().split() for i in range (n) ], int)

print (numpy.dot(arr,arr2))
