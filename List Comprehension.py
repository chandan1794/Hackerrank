X, Y, Z, N = [input() for _ in range(4)]  #taking 4 inputs using list comprehension technique

#running 3 loop inside if you look carefully 
#its like
#	> ans = []
#	> for a in range(X+1):
#	>	for b in range(Y+1):
#	>		for c in range(Z+1):
#	>			if a+b+c != N:
#	>				ans.append([a,b,c])
#
####################################################
ans = [[a,b,c] for a in range(X+1) for b in range(Y+1) for c in range(Z+1) if a+b+c != N] 
print ans
