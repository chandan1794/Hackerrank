import numpy

N,M= raw_input().split(" ")
N = int(N)
M = int(M)

list = [] #comprehension
							#assigns 0 to all the M values
for i in range(N):
	x = raw_input().split(" ")
	x = [int(i) for i in x]
	list.append(x)

#print list
min_max = numpy.max(numpy.min(list,1))
# min = numpy.min(list,1)
# max = numpy.max(min)
# print min,max
print min_max