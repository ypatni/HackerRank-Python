import numpy

arr = list(map(float, input().split()))
my_array = numpy.array(arr)
numpy.set_printoptions(sign = " ")
print (numpy.floor(my_array))
print (numpy.ceil(my_array))
print (numpy.rint(my_array))