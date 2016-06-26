# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
N = int(raw_input())
j = 0
dict3 ={}
marks = []
while j<N:
	name, x, y, z = raw_input().split(" ")
	marks.extend([float(x),float(y),float(z)])
	avg = sum(marks)/len(marks)
	# print(marks)
	# print(sum(marks))
	# print(len(marks))
	dict3[name] = avg
	j = j+1
	marks = [] 
query = raw_input()
print(format(dict3[query],'.2f'))
