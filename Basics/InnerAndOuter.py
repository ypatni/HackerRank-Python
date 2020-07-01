import numpy
  
arr = numpy.array([input().split() ], int)
arr2 = numpy.array([input().split() ], int)

print (numpy.inner(arr,arr2)[0][0])
print(numpy.outer(arr,arr2))