N,M= raw_input().split(" ")
N = int(N)
M = int(M)

list = [0 for i in range(M)] #comprehension
							#assigns 0 to all the M values
for i in range(N):
	x = raw_input().split(" ")
	list = [list[i]+int(x[i]) for i in range(M)]

prod = reduce(lambda x,y:x*y,list)
print prod
