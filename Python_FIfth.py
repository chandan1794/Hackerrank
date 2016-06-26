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

mean = numpy.mean(list,1)
var = numpy.var(list,0)
std = numpy.std(list)
# print min,max
print(mean)
print(var)
print(std)